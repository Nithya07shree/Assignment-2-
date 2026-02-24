# get user input
n = int(input("How many numbers do you have?  "))

# initialie values
sumNum=0
maxNum=-999999999
minNum=999999999

# calculate sum, min and max nums along with receiving user input
for i in range(1,n+1):
    num = float(input(f"Enter number {i}: "))
    
    sumNum+=num
    if num>maxNum:
        maxNum = num
    if num<minNum:
        minNum=num

if n==0:
    avgNum = 0
else:
    avgNum = sumNum / n

# print results
print(f"Sum: {sumNum}")
print(f"Average: {avgNum}")
print(f"Maximum number: {maxNum}")
print(f"Minimum number: {minNum}")