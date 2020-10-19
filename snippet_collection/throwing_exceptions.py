"""
Notes:
Throwing Exceptions 
    * "Throws" - Keyword in the method signature that states that we'll handle 
    the error higher up in the program 
    * Throw method can be used when the Dev know something is wrong with the program
    * Use this if something is wrong with the program that the computer doesn't 
    realize is wrong
        * Throw exception
        * Try-Catch block
    * Throw(Java) == Raise(Python)
"""

"""
Problem: Write a Calculator class with a single method: int power(int,int). 
The power method takes two integers,  and , as parameters and returns the integer 
result of . If either  or  is negative, then the method must throw an exception 
with the message: n and p should be non-negative.
"""

class Calculator:
    def power(self, n, p):
        if n < 0 or p < 0:
            raise Exception("n and p should be non-negative")
        else:
            return pow(n, p)
myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   