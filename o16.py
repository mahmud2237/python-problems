'''
Problem:
Calculate the sum of all integers from 1 to N using a loop.

Constraints:

1 <= N <= 10^5

Input Format: An integer 'N' representing the upper limit of the range for which the sum needs to be calculated.

Output Format:An integer, representing the sum of all numbers from 1 to N.

Sample Examples:

Input: 5

Output: 15

Explanation: The sum of numbers from 1 to 5 is 1 + 2 + 3 + 4 + 5 = 15.


Input: 10

Output: 55

Explanation: The sum of numbers from 1 to 10 is 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55.
'''

#========== User's Code Starts Here ==========
def sumOfNaturalNumbers(n):
    i = 1
    j = 0
    while i <= n:
        j += i
        i += 1
    return j

n = int(input())
print(sumOfNaturalNumbers(n))


    
#========== User's Code Ends Here ==========
