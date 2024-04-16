'''
Ramu needs your assistance in adding two numbers. Can you help him?
Input: You are given two numbers, `a` and `b`.

Output: Print the sum of these two numbers.

Example:
Input:
7 -3

Output:
4

Explanation:
Ramu wants to add 7 and -3. The sum of these numbers is 7 + (-3) = 4.
'''

#========== User's Code Starts Here ==========
'''
    Adds two numbers and prints the sum.
    :param a: The first number.
    :param b: The second number.
'''
def add_numbers(a, b):
    # Your implementation to add two numbers and print the result
    print(a + b)


def main():
    a, b = map(int, input().split())
    add_numbers(a, b)


#========== User's Code Ends Here ==========
