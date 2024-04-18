'''
Problem:
Write a program to print whether a given number is an Armstrong number or not..
(Armstrong number is a number in which all the sum of cubes of digits is equal to the number

Example:-
Input
n=153

Output
true

Logic - 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 1 +125 + 27 = 153 which is equal to the original number )

Input
123

Output
false

Logic - 123 is not an Armstrong number because 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36 which is not equal to the original number )
'''

#========== User's Code Starts Here ==========

def check_armstrong(n):
    """Function to check whether a number is an armstrong number or not
    Print true if yes else false """
    num_of_digits = len(str(n))
    temp = n 
    sumOfCube = 0
    while temp > 0:
        digit = temp % 10
        sumOfCube = sumOfCube + digit ** num_of_digits
        temp = temp // 10
    result = "true" if n == sumOfCube else "false"
    print(result)
    
    
    """Dont change anything below. If changed click on reset."""
def main():
    a=int(input())
    check_armstrong(a)
    
main()
    
#========== User's Code Ends Here ==========
