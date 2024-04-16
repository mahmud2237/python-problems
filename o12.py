'''
Problem:

Design a program to assign grades to students based on the following criteria:

- Students scoring less than or equal to 50 should be awarded a "D" grade.

- Students scoring above 50 but below 60 should receive a "C" grade.

- Students with marks between 60 to 75 should be assigned a "B" grade.

- Students scoring greater than 75 should be granted an "A" grade.


Example: Suppose the program is given the following student scores:

45

58

70

80


The program should output the corresponding grades for each student:

D

C

B

A



Note you will be just given one Input and you just need to output one grade
'''

#========== User's Code Starts Here ==========
def assign_grades(n):
    # Your implementation to assign grades based on the given criteria
    # Output the corresponding grade
    if(n>75):
        print("A")
    elif(60<=n <75):
        print("B")
    elif(50<n<60):
        print("C")
    elif(n<=50):
        print("D")

def main():
    a = int(input())
    print(assign_grades(a))
    

#========== User's Code Ends Here ==========
