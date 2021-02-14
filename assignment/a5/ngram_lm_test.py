from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import ngram_lm

import copy
import numpy as np
import unittest


class TestAddKTrigramLM(unittest.TestCase):
    def setUp(self):
        self.lm = ngram_lm.AddKTrigramLM('there be here there be dragons'.split())

    def test_counts(self):
        self.assertEqual(3, len(self.lm.counts))
        self.assertSetEqual(set([
            ('there', 'be'),
            ('be', 'here'),
            ('here', 'there')]), set(self.lm.counts.keys()))
        self.assertDictEqual({
            'here': 1.0,
            'dragons': 1.0}, self.lm.counts[('there', 'be')])

    def test_words(self):
        self.assertSetEqual(set([
            'there', 'be', 'here', 'dragons']),
            set(self.lm.words))
        self.assertEqual(4, self.lm.V)

    def test_context_totals(self):
        self.assertEqual(2, self.lm.context_totals[('there', 'be')])
        self.assertEqual(1, self.lm.context_totals[('be', 'here')])

    def test_next_word_proba_no_smoothing(self):
        self.lm.set_live_params(k=0.0)

        unseen_context_error_msg = """
LM with k=0 should either crash on unseen context with a ZeroDivisionError, or
return a plausible alternative probability estimate. If the latter, please
justify your choice in your code."""
        try:
            p = self.lm.next_word_proba('w266', ['hello', 'world'])
            self.assertTrue(np.isclose(1.0/self.lm.V, p) or np.isclose(0.0, p),
                            msg=unseen_context_error_msg)
        except Exception as e:
            self.assertIsInstance(e, ZeroDivisionError,
                                  msg=unseen_context_error_msg)

        pp = self.lm.next_word_proba('w266', ['there', 'be'])
        self.assertTrue(isinstance(pp, float))

        self.assertAlmostEqual(0,
                self.lm.next_word_proba('w266', ['there', 'be']))
        self.assertAlmostEqual(0.5,
                self.lm.next_word_proba('dragons', ['there', 'be']))
        self.assertAlmostEqual(1.0,
                self.lm.next_word_proba('be', ['here', 'there']))

    def test_next_word_proba_k_exists(self):
        self.lm.set_live_params(k=10.0)

        pp = self.lm.next_word_proba('w266', ['there', 'be'])
        self.assertTrue(isinstance(pp, float))

        self.assertAlmostEqual(10. / 40.,
                self.lm.next_word_proba('w266', ['hello', 'world']))
        self.assertAlmostEqual(11. / 42.,
                self.lm.next_word_proba('dragons', ['there', 'be']))

    def test_no_mutate_on_predict(self):
        self.lm.set_live_params(k=10.0)

        lm_copy = copy.deepcopy(self.lm)

        _ = self.lm.next_word_proba('w266', ['hello', 'world'])
        _ = self.lm.next_word_proba('dragons', ['there', 'be'])

        self.assertEqual(lm_copy, self.lm,
                         msg="lm_copy != self.lm. Calls to next_word_proba " +
                         "should not modify language model parameters!")

