import re
import math

def memo(fn):
  cache = {}
  def docache(arg, vocab):
    if arg in cache:
      return cache[arg]
    val = fn(arg, vocab)
    cache[arg] = val
    return val
  return docache

@memo
def segment(text, vocab):
  if not text: return []
  candidates = ([first]+segment(rem, vocab) for first, rem in splits(text))
  return max(candidates, key=lambda w: Pwords(w, vocab))

def splits(text, L=20):
  return [(text[:i+1], text[i+1:])
          for i in range(min(len(text), L))]

def Pw(w, vocab):
    if w in vocab.unigram_counts:
        return math.log(vocab.unigram_counts[w]) - math.log(vocab.num_unigrams)
    else:
        return math.log(vocab.num_unigrams) - 100*len(w)

def Pwords(words, vocab):
  return sum(Pw(w, vocab) for w in words)
