"""
PALINDROME CHECKER (Question 17)
INPUT: number/word
OUTPUT: original number, reversed number, result (is palindrome/ not palindrome)
"""

# get user input
val = input("Enter word/number: ")

# reverse the string for reversed value
# rev = val[::-1]
rev=""
for i in val:
    rev = i+rev

print(f"Original: {val}")
print(f"Reversed: {rev}")

# check for palindrome
if val.lower() == rev.lower():
    print("Result: PALINDROME")
else:
    print("Result: NOT PALINDROME")