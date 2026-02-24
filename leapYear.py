"""
LEAP YEAR CHECKER (Question 8)
INPUT: year number
OUTPUT: leap year / not leap year, reason
"""
def isLeapYear(y):
    if y%400==0:
        return "a", "it is divisible by 400"
    if y%100==0:
        return "not a", "it is divisible by 100 but not 400"
    if y%4==0:
        return "a", "it is divisible by 4 and not 100"
    return "not a", "it is not divisible by 4"

def check():
    while True:
        year = input("Enter year (or 'q' to quit): ")
        if year == 'q' or year == 'Q':
            print("Exiting...")
            break
        
        if not year.isdigit():
            print("Not a valid year, try again!")
            continue
        status, reason = isLeapYear(int(year))
        print(f"{year} is {status} leap year because {reason}")

check()