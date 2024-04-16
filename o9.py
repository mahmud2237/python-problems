'''
Watch this video on Switch case to understand the various terminologies of switch case :- Video_Link

People who code in python just understand the Algorithm and submit("Points will be given afterwards")


Given the Day number, print the Day name in lower case corresponding to it by using the help of switch statement.

Note: Day 1 - is monday.

If the day is not valid example 1> day >7 then print invalid

Input :-

Day - 3

Output :-

wednesday
'''

#========== User's Code Starts Here ==========
def weekday_name(n):
    if n ==1:
        print("monday")
    elif n==2:
        print("tuesday")
    elif n==3:
        print("wednesday")
    elif n==4:
        print("thursday")
    elif n==5:
        print("friday")
    elif n==6:
        print("saturday")
    elif n==7:
        print("sunday")
    else:
        print("invalid")

def main():    
    a = int(input())
    weekday_name(a)
main()

#========== User's Code Ends Here ==========
