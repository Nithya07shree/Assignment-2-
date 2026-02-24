# individual multiple tables
# get user input
num = int(input("Enter number: "))
endNum = int(input("Enter range (end): "))

# print the multiplication table
print(f"===Multiplication Table for {num}===")
for i in range(1,endNum+1):
    print(f"{num} x {i} = {num*i}")
    
# 1 to 10 multiplication tables
print("="*80)

# first row
print("     ",end="")
for i in range(1,11):
    print(f"{i}", end="\t")
print()
print("="*80)

# write multiplication tables (next rows)\

for row in range(1,11):
    # print row number
    print(f"{row}  | ",end="")
    # print tables
    for i in range(1,11):
        print(f"{row*i}",end="\t")
    print()