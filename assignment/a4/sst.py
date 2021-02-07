from __future__ import print_function
from __future__ import division

import os
import collections

import numpy as np
import pandas as pd
import nltk
from nltk.tree import Tree

from w266_common import utils, vocabulary
from w266_common import treeviz

# Colors from http://nlp.stanford.edu:8080/sentiment/rntnDemo.html
sst_node_colors = {'0':"#67001f", '1':"#f4a582",
                   '2':"#f7f7f7",
                   '3':"#92c5de", '4':"#052061"}
# Style function to color nodes when visualizing trees.
def sst_node_style(node):
    if not treeviz.is_tree(node):
        return {}
    return dict(style="filled",
                fontcolor=("#ffffff" if (node.label() in ['0', '4']) else "#000000"),
                fillcolor=sst_node_colors.get(node.label(), '#ffffff'),
                width=0.5, height=0.5)

def download_sst(output_dir="data"):
    import wget
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    url = "https://nlp.stanford.edu/sentiment/trainDevTestTrees_PTB.zip"
    return wget.download(url, out=output_dir)

class SSTDataset(object):

    Example_fields = ["tokens", "ids", "label", "is_root", "root_id"]
    Example = collections.namedtuple("Example", Example_fields)

    @staticmethod
    def get_lines(zipped_filename, split):
        import zipfile
        with zipfile.ZipFile(zipped_filename) as arx:
            with arx.open("trees/{:s}.txt".format(split)) as fd:
                return fd.readlines()

    @staticmethod
    def parse_line(sexp):
        if isinstance(sexp, bytes):
            sexp = sexp.decode("utf-8")
        return nltk.tree.Tree.fromstring(sexp)

    def canonicalize(self, raw_tokens):
        wordset=(self.vocab.wordset if self.vocab else None)
        return utils.canonicalize_words(raw_tokens, wordset=wordset)

    def get_trees(self, split):
        return [SSTDataset.parse_line(sexp) for sexp in
                SSTDataset.get_lines(self.zipped_filename, split)]

    def tree_to_example(self, tree, is_root, root_id):
        tokens = self.canonicalize(tree.leaves())
        ids = self.vocab.words_to_ids(tokens)
        label = int(tree.label())
        return SSTDataset.Example(tokens, ids, label, is_root, root_id)

    def recursive_extract_phrases(self, tree, output_list, is_root, root_id):
        if not isinstance(tree, Tree):
            return
        output_list.append(self.tree_to_example(tree, is_root, root_id))
        for subtree in tree:
            self.recursive_extract_phrases(subtree, output_list,
                                           is_root=False, root_id=root_id)

    def trees_to_dataframe(self, trees):
        examples = []
        for i, tree in enumerate(trees):
            self.recursive_extract_phrases(tree, examples, is_root=True,
                                           root_id = i)
        df = pd.DataFrame.from_records(examples, columns=SSTDataset.Example_fields)
        if self.label_scheme == "binary":
            # Drop 'neutral' class and collapse others to pos / neg
            df = df[df['label'] != 2]
            df['label'] = df['label'].map(lambda y: 1 if y > 2 else 0)
        return df

    def process(self, label_scheme="binary"):
        """Process trees to DataFrame, using the specified label scheme.

        Args:
            label_scheme: (string) "binary" or "fine" (5-class)
        """
        self.label_scheme = label_scheme
        if self.label_scheme == "binary":
            self.target_names = [0,1]
        elif self.label_scheme == "fine":
            self.target_names = [0,1,2,3,4]
        else:
            raise ValueError("Error: invalid label scheme {:s}".format(label_scheme))

        # Process trees to a DataFrame managing each split
        print("Processing to phrases... ", end=" ")
        self.train = self.trees_to_dataframe(self.train_trees)
        self.dev   = self.trees_to_dataframe(self.dev_trees)
        self.test  = self.trees_to_dataframe(self.test_trees)
        print("Done!")
        print("Splits: train / dev / test : {:,} / {:,} / {:,}".format(len(self.train),
                                                                       len(self.dev),
                                                                       len(self.test)))
        assert(set(self.train.label.unique()) == set(self.target_names))

        # Verify number of root phrases after filtering
        if self.label_scheme == "binary":
            assert(sum(self.train.is_root) == 6920)
            assert(sum(self.dev.is_root)   == 872)
            assert(sum(self.test.is_root)  == 1821)
        else:
            assert(sum(self.train.is_root) == 8544)
            assert(sum(self.dev.is_root)   == 1101)
            assert(sum(self.test.is_root)  == 2210)

        return self

    def __init__(self, V=10000):
        self.vocab = None
        self.zipped_filename = "data/sst/trainDevTestTrees_PTB.zip"
        self.target_names = None  # set by self.process()

        # Download datasets
        if not os.path.isfile(self.zipped_filename):
            data_dir = os.path.dirname(self.zipped_filename)
            print("Downloading treebank to {:s}".format(data_dir))
            self.zipped_filename = download_sst(data_dir)
        print("Loading SST from {:s}".format(self.zipped_filename))

        self.train_trees = self.get_trees("train")
        print("Training set:     {:,} trees".format(len(self.train_trees)))
        self.dev_trees = self.get_trees("dev")
        print("Development set:  {:,} trees".format(len(self.dev_trees)))
        self.test_trees = self.get_trees("test")
        print("Test set:         {:,} trees".format(len(self.test_trees)))

        # Verify that number of sentences matches the published size.
        assert(len(self.train_trees) == 8544)
        assert(len(self.dev_trees)   == 1101)
        assert(len(self.test_trees)  == 2210)

        # Build vocabulary over training set
        print("Building vocabulary - ", end="")
        train_words = utils.flatten(self.canonicalize(t.leaves())
                                    for t in self.train_trees)
        self.vocab = vocabulary.Vocabulary(train_words, size=V)
        print("{:,} words".format(self.vocab.size))

    def get_filtered_split(self, split='train', df_idxs=None, root_only=False):
        if not hasattr(self, split):
            raise ValueError("Invalid split name '%s'" % name)
        df = getattr(self, split)
        if df_idxs is not None:
            df = df.loc[df_idxs]
        if root_only:
            df = df[df.is_root]
        return df

    def as_padded_array(self, split='train', max_len=40, pad_id=0,
                        root_only=False, df_idxs=None):
        """Return the dataset as a (padded) NumPy array.

        Longer sequences will be truncated to max_len ids, while shorter ones
        will be padded with pad_id.

        Args:
          split: 'train' or 'test'
          max_len: maximum sequence length
          pad_id: id to pad shorter sequences with
          root_only: if true, will only export root phrases
          df_idxs: (optional) custom list of indices to export

        Returns: (x, ns, y)
          x: [num_examples, max_len] NumPy array of integer ids
          ns: [num_examples] NumPy array of sequence lengths (<= max_len)
          y: [num_examples] NumPy array of target ids
        """
        df = self.get_filtered_split(split, df_idxs, root_only)
        x, ns = utils.pad_np_array(df.ids, max_len=max_len, pad_id=pad_id)
        return x, ns, np.array(df.label, dtype=np.int32)

    def as_sparse_bow(self, split='train', root_only=False, df_idxs=None):
        from scipy import sparse
        df = self.get_filtered_split(split, df_idxs, root_only)
        x = utils.id_lists_to_sparse_bow(df['ids'], self.vocab.size)
        y = np.array(df.label, dtype=np.int32)
        return x, y

