#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from score import CompletedScoreCard, ScoreCard, ExcessFramesException


class NegativeBowlingTests(unittest.TestCase):

    def test_excess_frames(self):
        results = ["X","X","X","X","X","X","X","X","X","X","XXX"]
        self.assertRaises(ExcessFramesException, CompletedScoreCard,
                          ScoreCard([]), results)


if __name__ == '__main__':
    unittest.main()