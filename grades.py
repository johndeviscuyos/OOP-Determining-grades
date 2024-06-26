

class grades():
    def __init__(self):
        self.grades = 0
    def input_grade(self):
        while True:
            try:
                self.grades = int(input('Enter Grade:'))
                if 0<=self.grades<=100:
                    break
                else:
                    return"invalid grade"
            except ValueError:
                return"invalid grade"

    def display_grades(self):
        if self.grades >= 75:
            print ("Passed")
        else:
            print ("Fail")


g1 = grades()
g1.input_grade()
g1.display_grades()
