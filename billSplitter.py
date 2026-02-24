"""
BILL SPLITTER (Question 5)
INPUT: total bill amount, Number of people, Tax percentage, Tip percentage
OUTPUT: Subtotal, Tax amount, Bill after tax, Tip amount, Total bill, Amount per
person
"""

# get user inputs
totalBill = float(input("Enter total bill: "))
people = int(input("Enter number of people: "))
taxPercent = float(input("Tax Percentage: "))
tipPercent = float(input("Tip Percentage: "))

# print bill details
print()
print("=====BILL BREAKDOWN=====")
print(f"Subtotal    : Rs.{totalBill}")
tax= taxPercent*totalBill/100
print(f"Tax ({taxPercent}%) : Rs.{tax}")
totalBill = totalBill+tax
print(f"After Tax:  : Rs.{totalBill}")
tip = tipPercent*totalBill/100
print(f"Tip ({tipPercent}%) : Rs.{tip}")
totalBill = totalBill+tip
print(f"Total       : Rs.{totalBill}")
print(f"Per person  : Rs.{totalBill/people}")