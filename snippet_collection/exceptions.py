"""
Notes:
Exceptions --> "Throwing an Exception"
    * Creates error object when problem with code
        * Has error type
        * State of program
        * How we get error messages in console
    * Try-Catch block to solve error
    * Outputs controlled error message vs computer freaking out
    * Can have multiple catches
    * End with finally (Java)
    * Try->Except->Else (Python)
        * Can also do try->except->finally
        * Catch(Java) == Except(Python)
"""

"""
Problem:
"""

import sys

S = input().strip()

try:
    intVal = int(S)
    print(intVal)
except ValueError:
    print("Bad String")
