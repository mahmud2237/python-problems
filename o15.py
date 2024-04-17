'''
Problem:
By using while loop and continue statement
Print all number from 1 to n but then it should not be divisible by 5
Example:-
Input:-
n=7

output:-
1
2
3
4
6
7
'''

#========== User's Code Starts Here ==========
def print_output(n):
    """Print all numbers from 1 to n except the ones divisible by 5
    use the help of continue statement to leverage this  """
    i = 1
    while(i<=n):
        if(i%5==0):
            i += 1
            continue
        print(i)
        i += 1
    
    """Dont change anything below. If changed click on reset."""
def main():
    n=int(input())
    print_output(n)
    
main()
    
#========== User's Code Ends Here ==========
