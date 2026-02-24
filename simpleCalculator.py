"""
SIMPLE CALCULATOR (Question 2)
INPUT: two numbers
OUTPUT: result of Addition, Subtraction, Multiplication, Division, Modulus, Exponentiation
"""
# get user inputs
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

# print results
print("Results:")
    
print(f"{x}+{y}={x+y}") # addition
print(f"{x}-{y}={x-y}") # subtraction
print(f"{x}*{y}={x*y}") # multiplication
# division
print(f"{x}/{y}={x/y}") if y!=0 else print(f"Division by zero error, {x}/{y} is not possible")
# modulo operator
print(f"{x}%{y}={x%y}") if y!=0 else print(f"Division by zero error, {x}%{y} is not possible")
print(f"{x}^{y}={x**y}") # exponentiation

# define the mathematical operations
# operations = {
#     '+': lambda x,y:x+y,
#     '-': lambda x,y:x-y,
#     '*': lambda x,y:x*y,
#     '/': lambda x,y:x/y if y!=0 else "Division by zero error",
#     '%': lambda x,y:x%y if y!=0 else "Division by zero error",
#     '^': lambda x,y:x**y,
# }
# for oprn, fun in operations.items():
#     print(f"{x} {oprn} {y} = {fun(x,y)}")