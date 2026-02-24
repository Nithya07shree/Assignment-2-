def calcAndPrint(m1,m2,m3,m4,m5):
    # check validity
    if m1<0 or m2<0 or m3<0 or m4<0 or m5<0:
        print("Values cannot be zero")
        return
    # total marks
    totalMarks = m1+m2+m3+m4+m5
    # percentage
    percentage = totalMarks*100/500
    # grade
    if percentage>=90:
        grade="A+ (Outstanding)"
    elif percentage>=80:
        grade = "A (Excellent)"
    elif percentage>=70:
        grade = "B (Good)"
    elif percentage>=60:
        grade = "C (Average)"
    elif percentage>=50:
        grade = "D (Pass)"
    else:
        grade = "F (Fail)"
    # result
    if m1>=40 and m2>=40 and m3>=40 and m4>=40 and m5>=40:
        result = "Pass"
    else:
        result = "Fail"
    
    # print data
    print("===Student Grade Report===")
    print(f"Individual Marks : {m1}, {m2}, {m3}, {m4}, {m5}")
    print(f"Total marks      : {totalMarks}")
    print(f"Percentage       : {percentage}")
    print(f"Grade            : {grade}")
    print(f"Final Result     : {result}")


# get individual marks
m1 = int(input("Enter marks for subject 1: "))
m2 = int(input("Enter marks for subject 2: "))
m3 = int(input("Enter marks for subject 3: "))
m4 = int(input("Enter marks for subject 4: "))
m5 = int(input("Enter marks for subject 5: "))

# call function to print data
calcAndPrint(m1,m2,m3,m4,m5)