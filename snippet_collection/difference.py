"""
Notes:
"""

"""
Problem:
"""

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
    # Add your code here
    def computeDifference(self):
        maxEl = 101
        minEl = 0
        for el in self.__elements:
            if el > minEl:
                minEl = el
            if el < maxEl:
                maxEl = el
        self.maximumDifference = minEl - maxEl

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)