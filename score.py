#!/usr/bin/python
# -*- coding: utf-8 -*-


class frame:

    def __init__(self, index, result, score, total):
        self.index = index
        self.result = result
        self.score = score
        self.total = total

    def __repr__(self):
        return 'Frame: <%s: %s, %s, %s>' % (self.index, self.result,
                self.score, self.total)

# Score is a list of frames
class ScoreCard:

    def __init__(self, frames):
        self.frames = frames

    def size(self):
        if self.frames:
            return len(self.frames)
        else:
            return 0


class ExcessFramesException(Exception):
    pass

# Returns a scorecard given a list of results 
def CompletedScoreCard(scorecard, results):
    if not results:
        return scorecard
    if len(results) > 10:
        raise ExcessFramesException('Frames in game exceded')
