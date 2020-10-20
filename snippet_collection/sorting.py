"""
Notes:
Sorting
    * Pointers - Variable that store the address of another variable in memory. They point to the location of a value
        * Think of an address
        * To get the value from the location, you have to go to it.  This is called Dereferencing a pointer.
        * Referenced datatype - has a pointer to the memory location 
    * Enum - Special datatype that allows for a variable to be one of a set pre-defined constants
        * It is a preset value
        * They must be capitalizied 
    * Aliases - How to get two variables to relate to each other
        * Think of Peter Parker and Spider Man
"""

"""
Problem:
Given an array, a, of size n distinct elements, sort the array in ascending order using the Bubble Sort algorithm. Once sorted, print the 3 lines at the end:
"""
import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Initialize variable to count the total number of swaps
totalNumberOfSwaps = 0
# Bubble Sort Algorithm
# Run the algorithm n times because we only need to sort through the size of the array
for i in range(n):
    numberOfSwaps = 0;
    # Go through the array to compare each element to the next one until n-1, that way we don't compare n to n+1 and get an out of bounds error.
    for j in range(n-1):
        # For the comparison, if the element is out of order it will swap them and then increment the number of swaps
        if a[j] > a[j + 1]:
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp
            numberOfSwaps += 1
    # Adds each swap made to the totalNumberOfSwaps variable every time a swap is made
    totalNumberOfSwaps += numberOfSwaps
        
        # If no elements are swapped through this traversal, the array is sorted and we can exit the for loop
    if numberOfSwaps == 0:
        break

# Print 'Array is sorted in 'numSwaps'(number of swaps that took place) swaps.'
print('Array is sorted in ' + str(totalNumberOfSwaps) + ' swaps.')
# Print 'First Element: 'firstElement'(where firstElement is the first element of the array) 
print('First Element: ' + str(a[0]))
# Print 'Last Element: 'lastElement'(where lastElement is the last element of the array) 
print('Last Element: ' + str(a[n-1]))