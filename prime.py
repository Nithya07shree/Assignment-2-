# single number check
def isPrime(num):
    if num<2:
        return False
    for i in range(2,(num//2)+1):
        if num%i==0:
            return False
    return True
        
# input for single prime number
num = int(input("Enter a number: "))
if isPrime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is NOT a prime number.")


# print range of prime numbers
def primeRange(start, end):
    print(f"Prime numbers between {start} and {end}: ",end="")
    for i in range(start,end+1):
        if isPrime(i):
            print(i,end=", " if i<end-1 else "")


# input for printing prime numbers in a range of numbers
start = int(input("Enter starting range: "))
end = int(input("Enter ending range: "))

primeRange(start,end)