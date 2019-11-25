class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif 80 <= self.score < 90:
            return 'B'
        else:
            return 'C'


if __name__ == '__main__':

    lisa = Student('Lisa', 90)
    print(lisa.get_grade())
