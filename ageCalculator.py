""" 
 AGE CALCULATOR (Question 4)
 INPUT: current age
 OUTPUT: current age, age in months, age in days, age in hours, age in minutes and years until age 100.
 Attempted to perform precise calculations using exacct birth date (year-month-date)
"""

# get birth date, month and year
x = input("Enter your birthday in format yyyy-mm-dd:  ")

# check if leap year
def isLeapYear(y):
    return (y%4==0 and y%100!=0) or (y%400==0)

# check if input date is correct
def isValidDate(y,m,d):
    # check valid date range
    if not (1100<= y <=9999 and 1<= m <= 12 and 1<= d <31):
        return False
    # check for months with 30 days
    if m in [4,6,9,11] and d>=31: 
        return False
    # check for february month
    if m==2:
        if not isLeapYear(y):
            if m>=29:
                return False
        else:
            if d>28:
                return False
    # all checks passed
    return True

def currAge(cy,cm,cd, y,m,d):
    # add 30/31 if current date is less than birthdate
    if cd<d:
        cd+=30 if cm in [4,6,9,11] else 31
        cm-=1
    days = cd-d
    # add 12 if current month is less than birthmonth
    if cm<m:
        cm+=12
        cy-=1
    months = cm-m
    years = cy-y
    # print(f"{days} days, {months} months, {years} years")
    return years, months, days

def calculateme(x):
    y,m,d=[int(i) for i in x.split('-')]
    if not isValidDate(y,m,d):
        return False
    
    # get today's date
    from datetime import date
    today = date.today()
    cy,cm,cd = today.year, today.month, today.day
    # print today's date
    print(f"today is : {today}")
    
    # current age
    ageY,ageM,ageD=currAge(cy,cm,cd,y,m,d)
    print(f"Current Age: {ageY} years, {ageM} months, {ageD} days")
    
    # age in days
    ageDays = ageY*365+ageM*30+ageD+ageM//2
    # ageM//2 to balance months with 31 days
    print("Age in days = ",ageDays," days")
    
    # age in hours
    print("Age in hours = ",ageDays*24," hours")
    
    # age in minutes
    print("Age in minutes = ",ageDays*24*60," minutes")
    
    # time until age 100
    ageY,ageM,ageD=currAge(y+100,m,d,cy,cm,cd)
    print(f"Time until u might die: {ageY} years, {ageM} months, {ageD} days")
calculateme(x)