'''
Watch the following video on ternary operators :- Video_Link

Write a program to assume a value of marks and print whether a person has failed or passed using ternary Operator.


If Marks> =40 --> pass

ELSE ---> fail

Input:-

Marks =52

Ouput:-

pass
'''

#========== User's Code Starts Here ==========
def has_passed(marks):
    """write the code to find the whether a candidate has passed or failed 
    only print 'pass' or 'fail' """
    return "pass" if marks >= 40 else "fail"
    
    
    
    """Dont change anything below. If changed click on reset."""
def main():
    a = int(input())
    print(has_passed(a))
    
main()

#========== User's Code Ends Here ==========
