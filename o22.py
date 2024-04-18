'''
Problem:
Understand Continue from this video :- Link  and solve the question using continue jumping statement.
Write a program to print even numbers from 1 to n except numbers which are divisible by 4. 
Use Continue statement to avoid printing.
Input-
10

Output-
2
6
10
'''

#========== User's Code Starts Here ==========

def print_output(n):
    """Print all even numbers from 1 to n except the ones divisible by 4
    use the help of continue statement to leverage this  """
    for i in range(2, n+1, 2):
        if (i%4==0):
            continue
        print(i)
    
    """Dont change anything below. If changed click on reset."""
def main():
    n=int(input())
    print_output(n)
    
main()
#========== User's Code Ends Here ==========

"""

"""
