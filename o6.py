'''
Given a variable D (distance) write a program to print the cost associated with it as shown in the image:-
Here, Distance inputs below:

    0 through 100 => 5.00
    More than 100 but not more than 500 => 8.00
    More than 500 but less than 1000 => 10.00
    1000 or More => 12

Input:-

D = 700

Output:-

10
'''

#========== User's Code Starts Here ==========
def print_cost(d):
    """
    """
    if(0<=d<=100):
        return 5
    elif(100<d<=500):
        return 8
    elif(500<d<1000):
        return 10
    else:
        return 12
    
    
    
    
    """Dont change anything below. If changed click on reset."""
def main():
    d = int(input())
    print(print_cost(d))
    
main()

#========== User's Code Ends Here ==========
