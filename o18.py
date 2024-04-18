'''
Problem:
Write a program to return the reverse of a number .

Input:-
153 .

output:-
351
'''

#========== User's Code Starts Here ==========

def reverse(n):
    """ Function to return the reverse of a number n """
    """
        :type n: int
        :rtype: int
    """
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = (reversed_num * 10) + digit
        n = n // 10
    return reversed_num
    
    """Dont change anything below. If changed click on reset."""
def main():
    a = int(input())
    output = reverse(a)
    print(output)
    
main()
    
#========== User's Code Ends Here ==========
