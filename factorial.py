"""
FACTORIAL CALCULATOR (Question 14)
INPUT: input number for factorial  calculation
OUTPUT: step by step factorial calculation, result
"""
# get user input
num = int(input("Enter a number: "))

# check conditions
if num<0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("0! = 1")
else:
    fact=1
    seq=""
    
    for i in range(num,0,-1):
        fact*=i
        # add 'x' sign only until last number
        if i>1:
            seq = seq+ str(i)+ " x "
        else:
            seq+=str(i)

print(f"Factorial for {num} is: ") 
print(f"{num}! = {seq} = {fact}")