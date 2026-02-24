def temperatureConverter():
    while True:
        choice = input("Select an option (1-7): ")
        if choice == '7':
            print("Exiting convertor. See ya!!")
            break
        
        # check option number validity
        if choice not in ['1','2','3','4','5','6']:
            print("Invalid options chosen. Try again!!")
            continue
        
        # get initial value
        temp = float(input("Enter the initial temperature value: "))
        
        # Temperature Conversion
        if choice == "1":
            print(f"{temp} C is equal to {(temp * 9/5)+32} F")
        
        elif choice == "2":
            print(f"{temp} F is equal to {(temp-32)* 5/9} C")
        
        elif choice == "3":
            print(f"{temp} C is equal to {(temp+273.15)} K")
        
        elif choice == "4":
            print(f"{temp} K is equal to {temp-273.15} C")
        
        elif choice == "5":
            print(f"{temp} F is equal to {(temp-32)* 5/9 +273.15} K")
        
        elif choice == "6":
            print(f"{temp} K is equal to {(temp-273.15) * 9/5 +32} F")
        
        print()
        
print("-----Choose a convertion unit-----")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")
print("5. Fahrenheit to Kelvin")
print("6.  Kelvin to Fahrenheit")
print("7. Exit")

temperatureConverter()