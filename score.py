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

class IllegalResultException(Exception):
	pass    

def validateResult(result, scorecard_size):
    if len(result) == 1 and result != 'X' or len(result) > 3:
        raise IllegalResultException('Wrong result for frame no:',
                scorecard_size + 1, result)
    if scorecard_size != 9 and len(result) == 3:
        raise IllegalResultException('Wrong result for frame no:',
                scorecard_size + 1, result)
    if result[0] == 'X' and len(result) > 1:
        if scorecard_size < 9:
            raise IllegalResultException('Wrong result for frame no:',
                    scorecard_size + 1, result)
        elif len(result) != 3:
            raise IllegalResultException('Wrong result for frame no:',
                    scorecard_size + 1, result)

def scoreFrame(scorecard, result):
	scorecard_size = scorecard.size()
	validateResult(result, scorecard_size)
	
# Returns a scorecard given a list of results 
def CompletedScoreCard(scorecard, results):
    if not results:
        return scorecard
    if len(results) > 10:
        raise ExcessFramesException('Frames in game exceded')
    return CompletedScoreCard(scoreFrame(scorecard, results[0]),
                              results[1:])
