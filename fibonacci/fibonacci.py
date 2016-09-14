"""Paul Fordham | ptf06c """
#!/user/bin/env python
#from __future__ import print_function # print()

# generator function
def fibonacci_gen(fibSize):
    num1 = 0
    num2 = 1
    for i in range(fibSize):
        yield num1
        fib = num1 + num2
        num1 = num2
        num2 = fib

class Fibonacci:
    # constructor
    def __init__(self, sizeInput):
        self.count = 1
        self.num1 = 0
        self.num2 = 1
        self.fibSize = sizeInput
        self.nums = []

    # function to get fib nums
    def get_nums(self, isStr = False):
        if isStr:
            self.num1 = 0
            self.num2 = 1
            self.nums = []

        self.nums.append(self.num1)
        self.nums.append(self.num2)
        if not self.fibSize <= 2:
            for i in range(self.fibSize - 2):
                fib = self.num1 + self.num2
                self.num1 = self.num2
                self.num2 = fib
                self.nums.append(fib)
        if not isStr:
            print self.nums

    # define how to print object. aka print f. where f = Fibonacci(10)
    def __str__(self):
        self.get_nums(True)
        return "The first " + str(self.fibSize) + "Fibonacci numbers are " + str(self.nums)

    # setup iterator
    def __iter__(self):
        return self

    # tell iterator how to get next value
    def next(self):
        if self.count > self.fibSize:
            raise StopIteration
        else:
            self.count += 1
            fib = self.num1 + self.num2
            retVal = self.num1
            self.num1 = self.num2
            self.num2 = fib
            return retVal
