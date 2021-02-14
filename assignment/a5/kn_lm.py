from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

from collections import defaultdict
import numpy as np
from ngram_lm import BaseLM 

class KNTrigramLM(BaseLM):
    """Trigram LM with Kneser-Ney smoothing."""
    order_n = 3
    # For testing - do not modify.
    state_vars = ['delta', 'counts', 'type_contexts',
                  'context_totals', 'context_nnz', 'type_fertility',
                  'z_tf', 'words']

    def __init__(self, tokens):
        """Build our smoothed trigram model.

        This should be similar to the AddKTrigramLM.__init__ function, above,
        but will compute a number of additional quantities that we need for the
        more sophisticated KN model.

        See the documentation in the notebook for the KN backoff model
        definition and equations, and be sure to read the in-line comments
        carefully to understand what each data structure represents.

        Note the usual identification of variables:
          w : c : current word
          w_1 : w_{i-1} : b : previous word
          w_2 : w_{i-2} : a : previous-previous word

        There are two blocks of code to fill here. In the first one, you should
        fill in the inner loop to compute:
          self.counts         (unigram, bigram, and trigram)
          self.type_contexts  (set of preceding words for each word (type))

        In the second one, you should compute:
          self.context_totals  (as in AddKTrigramLM)
          self.context_nnz     (number of nonzero elements for each context)
          self.type_fertility  (number of unique preceding words for each word
                                      (type))

        The starter code will fill in:
          self.z_tf   (normalization constant for type fertilities)
          self.words  (list of words known to the model)

        Args:
          tokens: (list or np.array) of training tokens

        Returns:
          None
        """
        self.delta = 0.75
        # Raw counts over the corpus.
        # Keys are context (N-1)-grams, values are dicts of word -> count.
        # You can access C(w | w_{i-1}, ...) as:
        # unigram: self.counts[()][w]
        # bigram:  self.counts[(w_1,)][w]
        # trigram: self.counts[(w_2,w_1)][w]
        self.counts = defaultdict(lambda: defaultdict(lambda: 0))
        # As in AddKTrigramLM, but also store the unigram and bigram counts
        # self.context_totals[()] = (total word count)
        # self.context_totals[(w_1,)] = c(w_1)
        # self.context_totals[(w_2, w_1)] = c(w_2, w_1)
        self.context_totals = dict()
        # Also store in self.context_nnz the number of nonzero entries for each
        # context; as long as \delta < 1 this is equal to nnz(context) as
        # defined in the notebook.
        self.context_nnz = dict()

        # Context types: store the set of preceding words for each word
        # map word -> {preceding_types}
        self.type_contexts = defaultdict(lambda: set())
        # Type fertility is the size of the set above
        # map word -> |preceding_types|
        self.type_fertility = dict()
        # z_tf is the sum of type fertilities
        self.z_tf = 0.0


        # Iterate through the word stream once
        # Compute unigram, bigram, trigram counts and type fertilities
        w_1, w_2 = None, None
        for word in tokens:
            self.counts[()][word] += 1
            if w_1 is not None:
                self.counts[(w_1,)][word] += 1
                self.type_contexts[word].add(w_1)
                if w_2 is not None:
                    self.counts[(w_2,w_1)][word] += 1

            # Update context
            w_2 = w_1
            w_1 = word

        ##
        # We'll compute type fertilities and normalization constants now,
        # but not actually store the normalized probabilities. That way, we can compute
        # them (efficiently) on the fly.

        # Count the total for each context.
        self.context_totals = {k:float(sum(c.values())) for k,c in self.counts.items()}

        # Count the number of nonzero entries for each context.
        self.context_nnz = {k:len(c) for k,c in self.counts.items()}


        # Compute type fertilities, and the sum z_tf.
        self.type_fertility = {w:len(s) for w,s in self.type_contexts.items()}


        self.z_tf = float(sum(self.type_fertility.values()))


        # Freeze defaultdicts so we don't accidentally modify later.
        self.counts.default_factory = None
        self.type_contexts.default_factory = None

        # Total vocabulary size, for normalization
        self.words = list(self.counts[()].keys())
        self.V = len(self.words)

    def set_live_params(self, delta = 0.75, **params):
        self.delta = delta

    def kn_interp(self, word, context, delta, pw):
        """Compute KN estimate P_kn(w | context) given a backoff probability

        Your code should implement the absolute discounting equation from the
        notebook, using the counts computed in __init__(). Note that you don't
        need to deal with type fertilities here; this is handled in the
        next_word_proba() function in the starter code, below.

        Be sure you correctly handle the case where c(context) = 0, so as to not
        divide by zero later on. You should just return the backoff probability
        directly, since we have no information to decide otherwise.

        Be sure that you don't modify the parameters of the model in this
        function - in particular, you shouldn't (intentionally or otherwise)
        insert zeros or empty dicts when you encounter an unknown word or
        context. See note on dict.get() below.

        Args:
          word: (string) w in P(w | context )
          context: (tuple of string)
          delta: (float) discounting term
          pw: (float) backoff P_kn(w | less_context), precomputed

        Returns:
          (float) P_kn(w | context)
        """
        # Hint: self.counts.get(...) and self.context_totals.get(...) are
        # useful here. See note in dict_notes.md about how this works.
        c0 = self.counts.get(context, {}).get(word, 0)
        z0 = self.context_totals.get(context, 0)
        # If context is never seen, pass through backoff unchanged
        if z0 == 0: return pw
        # Interpolation factor alpha
        alpha = delta * (self.context_nnz.get(context, 0) / z0)
        pwc = max(0, c0 - delta)/z0
        return pwc + alpha * pw


    def next_word_proba(self, word, seq):
        """Compute next word probability with KN backoff smoothing.

        Args:
          word: (string) w in P(w | w_1 w_2 )
          seq: list(string) [w_1, w_2, w_3, ...]
          delta: (float) discounting term

        Returns:
          (float) P_kn(w | w_1 w_2)
        """
        delta = delta = self.delta
        # KN unigram, then recursively compute bigram, trigram
        pw1 = self.type_fertility.get(word, 0.0) / self.z_tf
        pw2 = self.kn_interp(word, tuple(seq[-1:]), delta, pw1)
        pw3 = self.kn_interp(word, tuple(seq[-2:]), delta, pw2)
        return pw3
