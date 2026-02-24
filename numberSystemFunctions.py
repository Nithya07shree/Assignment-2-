def factorial(n):
    if n<0:
        return "Factorial not defined for negative numbers"
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

def isPrime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def fibonacci(n):
    if n<=0:
        return "Invalid Input"
    elif n==1:
        return 0
    elif n==2:
        return 1
    a,b = 0,1
    for i in range(3,n+1):
        c=a+b
        a=b
        b=c
    return b

def sumDigits(n):
    total = 0
    while n>0:
        total += n%10
        n//=10
    return total

def reverseNum(n):
    rev=0
    while(n>0):
        digit=n%10
        rev=rev*10+digit
        n//=10
    return rev

def isArmstrong(n):
    temp=n
    digits=len(str(n))
    total=0
    
    while temp>0:
        digit = temp%10
        total+=digit**digits
        temp//=10
    return total==n

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a


def lcm(a,b):
    return (a*b)//gcd(a,b)

def isPerfectNumber(n):
    total=0
    for i in range(1,n):
        if n%i==0:
            total+=i
    return total==n

def menuFunction():
    while True:
        print("======NUMBER SYSTEM MENU======")
        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Number")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number")
        print("10. Exit")
        
        choice = input("Enter your choice(1-10): ")
        if choice =='10':
            print("Exiting...")
            break
        
        elif choice =='1':
            n= int(input("Enter number: "))
            print(f"Factorial: {factorial(n)}")
        
        elif choice =="2":
            n=int(input("Enter number: "))
            print("Prime: ","Yes" if isPrime(n) else "No")
        
        elif choice =="3":
            n=int(input("Enter number: "))
            print(f"Fibonacci: ",fibonacci(n))
        
        elif choice=="4":
            n=int(input("Enter number: "))
            print("Sum of digits: ", sumDigits(n))
        
        elif choice=="5":
            n=int(input("Enter number: "))
            print("Reversed number: ",reverseNum(n))
        
        elif choice =="6":
            n=int(input("Enter number: "))
            print("Armstrong: ", "Yes" if isArmstrong(n) else "No")
        
        elif choice =="7":
            a= int(input("Enter first number: "))
            b= int(input("Enter second number: "))
            print("GCD: ",gcd(a,b))
        
        elif choice =="8":
            a= int(input("Enter first number: "))
            b= int(input("Enter second number: "))
            print("LCM: ", lcm(a,b))
        
        elif choice =="9":
            n=int(input("Enter number: "))
            print("Perfect number: ", "Yes" if isPerfectNumber(n) else "No")
        
        else:
            print("Invalid choice!! Try again.")
            
menuFunction()