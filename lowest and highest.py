
class numbers():
    def __init__(self):
        self.numbers = []


    def get_numbers(self):
        numberss = input("Enter a number: ")
        split_numbers = numberss.split()
        self.numbers = [int(num) for num in split_numbers]


    def lowesthighest (self):
        if self.numbers:
            print (min(self.numbers))
            print (max(self.numbers))
        else:
            print("No numbers entered")

oddevens = numbers()
oddevens.get_numbers()
oddevens.lowesthighest()
numbers.lowesthighest()

