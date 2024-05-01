'''
Let's make an application, which is called a tip calculator. If the bill was $150.00, split between 5 people, with 10%, 12%, or 15% tip.
Each person should pay (150.00 / 5) * 1.12 = 33.6  (When tip is 12%)
First print it normally like the result 33.6
Then, Round the result to 2 decimal places = 33.60
'''

#========== User's Code Starts Here ==========
print("Hey there! Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip do you want to give? 10, 12 or 15? "))
people = int(input("How much people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
including_tip_total_bill = bill + total_tip_amount
bill_per_person = including_tip_total_bill / people

print(f"Normally the bill per person is ${bill_per_person}")

Final_round_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${Final_round_amount}")

#========== User's Code Ends Here ==========
