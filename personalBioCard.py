"""
PERSONAL BIO CARD (Question 1)
INPUT: not required
OUTPUT: a formatted bio data card
"""

def printCard(studentInfo):
    # print initial seperator box
    # used 45 as max wiidth of card
    print("="*45)
    print(f"|             STUDENT BIO CARD              |")
    print("="*45)
    
    # print student details
    for key, val in studentInfo.items():
        pad1 = " "*(10-len(key))
        content = f"{key}{pad1}: {val}"
        pad2 = " "*(45-len(content)-3)
        print(f"| {content}{pad2}|")
    
    # print final seperator line
    print("="*45)
        
# write or get student information
studentInformation = {
        "Name": "Avinash",
        "Age": "20 years",
        "Course": "Python Programming",
        "College": "Amit University",
        "Email": "avin@gmail.com"
    }    
# call printCard function to print the details
printCard(studentInformation)