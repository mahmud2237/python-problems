'''
Problem:
Understand the use case of break by going through this video - Link 
and solve the following question :-
Write a program to print all the numbers from 1 to n .If m is present in between the sequence then stop printing any other number and break out of the loop.

Input :-
n = 10 m = 4

Output :-
1
2
3
'''

#========== User's Code Starts Here ==========

def print_series(n,m):
    """Print the following series from 1 to n if m is present stop printing the series 
    Note print all the numbers in a seperate line """
    for i in range(1, n+1):
        if(i==m):
            break
        print(i)
            
    """Dont change anything below. If changed click on reset."""
def main():
    n=int(input())
    m=int(input())
    print_series(n,m)
    
main()
#========== User's Code Ends Here ==========

"""

"""
