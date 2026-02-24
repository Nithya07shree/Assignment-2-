def calculator():
    while True:
        print("=======SIMPLE CALCULATOR=======")
        print("1. Add")
        print("2. Subtract")
        print("3. MUltiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")
        
        choice = input("Enter your choice(1-7): ")
        if choice == "7":
            print("Exiting calculator... ")
            break
        if choice in ['1','2','3','4','5','6']:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            
            if choice =='1':
                result = a+b
            elif choice =='2':
                result = a-b
            elif choice =='3':
                result = a*b
            elif choice =='4':
                result = a/b if b!=0 else "Error! Division by zero not allowed."
            elif choice =='5':
                result = a%b if b!=0 else "Error! Modulus by zero not allowed."
            elif choice =='6':
                result = a**b
            
            print("Result: ",result)
        else:
            print("Invalid choice! try again")

calculator()