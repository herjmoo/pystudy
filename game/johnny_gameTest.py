class Calculator:
    def __init__(self, a):
        self.numberList = a
    def sum(self):
        self.result = 0
        for numbers in self.numberList:
            self.result = self.result + numbers
        return self.result
    def avg(self):
        total = self.sum()
        print(self.result)
        return total / len(self.numberList)

cal1 = Calculator([1,2,3,4,6])
print(cal1.avg())
print(cal1.sum())