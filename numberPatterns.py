print("Consider the following patterns")
print("======PATTERN 1======")
print("1")
print("1 2")
print("1 2 3")
print()
print("======PATTERN 2======")
print("1")
print("2 2")
print("3 3 3")
print()
print("======PATTERN 3======")
print("3 2 1")
print("2 1")
print("1")
print()
print("======PATTERN 4======")
print("   1")
print(" 1 2 1")
print("1 2 3 2 1")
print()

while True:
    choice = input("Enter a pattern number or 'q' to quit: ")
    if choice == "q":
        print("Leaving you with your peace. Bye!!")
        break
    
    if choice not in ['1','2','3','4']:
        print("This is invalid. Enter a correct number")
        continue
    
    n= int(input("Enter the pattern's height: "))
    
    # pattern 1
    if choice == "1":
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(j,end=' ')
            print() 
    # pattern 2
    elif choice == "2":
        for i in range(1,n+1):
            for j in range(i):
                print(i,end=" ")
            print()
    # pattern 3
    elif choice == "3":
        for i in range(n,0,-1):
            for j in range(i,0,-1):
                print(j,end=" ")
            print()
    # pattern 4
    elif choice == "4":
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(j,end=" ")
            for j in range(i-1,0,-1):
                print(j,end=" ")
            print()
