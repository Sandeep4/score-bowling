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


def getBallsScore(result):
    firstBallScore = 0
    secondBallScore = 0
    thirdBallScore = 0

    if result == 'XXX':
        firstBallScore = 10
        secondBallScore = 10
    elif result[0] == 'X':
        firstBallScore = 10
    else:
        try:
            firstBallScore = int(result[0])
        except Exception, e:
            raise IllegalResultException('Illegal value for result',
                    result)

        if result[1] == '/':
            secondBallScore = 10 - firstBallScore
        else:
            try:
                secondBallScore = int(result[1])
            except Exception, e:
                raise IllegalResultException('Illegal value for result'
                        , result)

    if len(result) == 3:
        if result[-1] == 'X':
            thirdBallScore = 10
        else:
            try:
                thirdBallScore = int(result[2])
            except Exception, e:
                raise IllegalResultException('Illegal value for result'
                        , result)

    return (firstBallScore, secondBallScore, thirdBallScore)


def scoreFrame(scorecard, result):
    scorecard_size = scorecard.size()
    validateResult(result, scorecard_size)
    (firstBallScore, secondBallScore, thirdBallScore) = \
        getBallsScore(result)

    changedFrames = []
    past1FrameTotal = 0
    if scorecard_size >= 1:
        past1FramesScore = scorecard.frames[-1].score
        past2FrameTotal = 0
        if scorecard_size >= 2:
            past2FrameTotal = scorecard.frames[-2].total

        if scorecard.frames[-1].result == 'X':
            if scorecard_size >= 2 and scorecard.frames[-2].result \
                == 'X':
                past2FrameScore = scorecard.frames[-2].score \
                    + firstBallScore
                past3FrameTotal = 0
                if scorecard_size >= 3:
                    past3FrameTotal = scorecard.frames[-3].total
                past2FrameTotal = past3FrameTotal + past2FrameScore
                changedFrames.append(frame(scorecard.frames[-2].index,
                        scorecard.frames[-2].result, past2FrameScore,
                        past2FrameTotal))

            past1FramesScore = scorecard.frames[-1].score \
                + firstBallScore + secondBallScore
        if scorecard.frames[-1].result[-1] == '/':
            past1FramesScore = scorecard.frames[-1].score \
                + firstBallScore
        past1FrameTotal = past2FrameTotal + past1FramesScore
        changedFrames.append(frame(scorecard.frames[-1].index,
                             scorecard.frames[-1].result,
                             past1FramesScore, past1FrameTotal))

    frameIndex = scorecard_size + 1

    frameScore = firstBallScore + secondBallScore + thirdBallScore
    if frameIndex == 1:
        frameTotal = frameScore
    else:
        frameTotal = past1FrameTotal + frameScore
    changedFrames.append(frame(frameIndex, result, frameScore,
                         frameTotal))

    if scorecard_size - (len(changedFrames) - 1) > 0:
        return ScoreCard(scorecard.frames[:scorecard_size
                         - (len(changedFrames) - 1)] + changedFrames)
    else:
        return ScoreCard(changedFrames)

# Returns a scorecard given a list of results
def CompletedScoreCard(scorecard, results):
    if not results:
        return scorecard
    if len(results) > 10:
        raise ExcessFramesException('Frames in game exceded')
    return CompletedScoreCard(scoreFrame(scorecard, results[0]),
                              results[1:])
