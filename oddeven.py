
class oddeven():
    def __init__(self):
        self.oddeven=None

    def get_oddeven(self):
        while True:
            try:
                self.oddeven= int(input("Enter a number:"))
                if self.oddeven %2 == 0 :
                    return "Even Number"
                else:
                    return "Odd Number"
            except ValueError:
                return "Invalid Input"

number = oddeven()
print(number.get_oddeven())