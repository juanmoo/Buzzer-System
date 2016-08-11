from Category import *
from GameSchedule import *

class ScoreSheet (dict):
    #Create Outcome Constants

    full_points = 0
    partial_points = 1
    no_points = 2
    penalty_points = 3

    outcomes = [full_points, partial_points, no_points, penalty_points]

    def __init__(self, schedule):
        self.schedule = schedule
        if not isinstance(schedule, GameSchedule):
            raise Exception('*** Invalid input. Input parameter must be of type \'GameSchedule\' ***')
        for category in schedule:
            if not isinstance(category, Category):
                raise Exception('*** Elements in schedule must be of type \'Category\' ***')
            outcomeList = []
            for i in range(category.getQuestionNumber()):
                outcomeList.append(0)
            self.update({category:outcomeList})

    def update (self, other):
        if not isinstance(other, dict):
            raise Exception('Other is not a dict.')
        #check if keys are of type 'Category'
        for category in other:
            if not isinstance(category, Category):
                raise Exception('Keys in the the score sheet must be of the type \'Category\'.')
            #check for valid initialization outcome codes.
            for outcome in other[category]:
                if not outcome in range(4):
                    raise Exception('Invalid outcome code.')
            super(ScoreSheet, self).update({category:other[category]})

    def setOutcome(self, category, qNum, outcome):
        if not isinstance(category, Category):
            raise TypeError(str(category)+' must be of type \'Category\'')
        assert qNum <= category.getQuestionNumber(), '*** Invalid Question Number ***'
        assert outcome in ScoreSheet.outcomes, "*** Invalid Outcome Code ***"
        self[category][qNum] = outcome


    def calculateScore(self, category):
        total = 0
        for outcome in self[category]:
            total += (1 if outcome != ScoreSheet.penalty_points else -1) * category.pointKey[outcome]
        return total


    def calculateTotalScore(self):
        total = 0
        for category in self.schedule:
            total += self.calculateScore(category)
        return total
