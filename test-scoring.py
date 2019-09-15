#!/usr/bin/python
# -*- coding: utf-8 -*-

from score import CompletedScoreCard, ScoreCard, ExcessFramesException, IllegalResultException
import unittest


class PositiveBowlingTests(unittest.TestCase):

    def test_strikes(self):
        results = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'XXX']
        finalScoreCard = CompletedScoreCard(ScoreCard([]), results)
        self.assertEqual(finalScoreCard.frames[-1].total, 300)

    def test_nearly_all_strikes(self):
        results = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X00']
        finalScoreCard = CompletedScoreCard(ScoreCard([]), results)
        self.assertEqual(finalScoreCard.frames[-1].total, 270)

    def test_scores(self):
        results = ['90', '90', '90', '90', '90', '90', '90', '90', '90', '90']
        finalScoreCard = CompletedScoreCard(ScoreCard([]), results)
        self.assertEqual(finalScoreCard.frames[-1].total, 90)

    def test_spares(self):
        results = ['5/', '5/', '5/', '5/', '5/', '5/', '5/', '5/', '5/', '5/5']
        finalScoreCard = CompletedScoreCard(ScoreCard([]), results)
        self.assertEqual(finalScoreCard.frames[-1].total, 150)

    def test_no_extra_point(self):
        results = ['5/']
        finalScoreCard = CompletedScoreCard(ScoreCard([]), results)
        self.assertEqual(finalScoreCard.frames[-1].total, 10)

    def test_game_example(self):
        results = ['X', '7/', '72', '9/', 'X', 'X', 'X', '23', '6/', '7/3']
        finalScoreCard = CompletedScoreCard(ScoreCard([]), results)
        self.assertEqual(finalScoreCard.frames[-1].total, 168)


class NegativeBowlingTests(unittest.TestCase):

    def test_excess_frames(self):
        results = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'XXX']
        self.assertRaises(ExcessFramesException, CompletedScoreCard,
                          ScoreCard([]), results)

    def test_bad_result(self):
        results = ['XX', '23', '6/', '7/']
        self.assertRaises(IllegalResultException, CompletedScoreCard,
                          ScoreCard([]), results)

    def test_incomplete_result(self):
    	results = ['X', '7/', '72', '9/', 'X', 'X', 'X', '23', '6/', 'XX']
        self.assertRaises(IllegalResultException, CompletedScoreCard,
                          ScoreCard([]), results)


if __name__ == '__main__':
    unittest.main()
