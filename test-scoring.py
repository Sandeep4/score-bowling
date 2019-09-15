#!/usr/bin/python
# -*- coding: utf-8 -*-

from score import CompletedScoreCard, ScoreCard, ExcessFramesException, IllegalResultException
import unittest



class NegativeBowlingTests(unittest.TestCase):

    def test_excess_frames(self):
        results = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'XXX']
        self.assertRaises(ExcessFramesException, CompletedScoreCard,
                          ScoreCard([]), results)

    def test_wrong_result(self):
        results = ['XX', '23', '6/', '7/']
        self.assertRaises(IllegalResultException, CompletedScoreCard,
                          ScoreCard([]), results)



if __name__ == '__main__':
    unittest.main()
