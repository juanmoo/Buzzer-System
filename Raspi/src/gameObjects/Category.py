class Category(object):
    idNumber = 0
    def __init__(self, name, questionNumber,full_points, partial_points, penalty_points):
        self.questionNumber = questionNumber
        self.idNumber = Category.idNumber
        Category.idNumber += 1
        self.name = name
        """
        pointKey stores the point values of the different types of question
        outcomes in the following manner:
            [0, full_points, partial_points, penalty_points]
        """
        self.pointKey = [full_points, partial_points, 0, penalty_points]
    def __lt__(self, other):
        assert isinstance(other, Category)
        return self.idNumber<other.idNumber

    def __str__ (self):
        return self.name+"-"+str(self.idNumber)

    def getQuestionNumber(self):
        return self.questionNumber
