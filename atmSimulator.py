"""
 SIMPLE ATM SIMULATOR (Question 10)
 INPUT: menu based (Check balance, Deposit money, Withdraw money, Exit)
 OUTPUT: balance and transaction status based on choice
 RULES: sufficient funds checked before withdrawl, minimum balance of Rs.500 is maintained,
        transaction messages ad updated balance printed after each transaction
"""

def atmSimulator():
    balance = 10000
    minBalance = 500
    while True:
        print("----Select an option----")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            print(f"Current Balance = {balance}")
        elif choice == "2":
            amount = int(input("Enter amount to deposit: "))
            if amount>0:
                balance+= amount
                print(f"Deposited Rs.{amount} successfully.")
                print(f"New balance is Rs.{balance}")
            else:
                print("Invalid amount")
        elif choice == "3":
            amount = int(input("Enter amount to withdraw: "))
            if amount > balance:
                print(f"Insufficient balance!!")
            elif (balance-amount)<minBalance:
                print(f"Cannot withdraw funds. You need to have a min balance of Rs.{minBalance}")
            elif amount <=0:
                print("Invalid amount")
            else:
                balance-=amount
                print(f"Withdrawl successful. New balance is Rs.{balance}")
        elif choice =="4":
            print("Thank you for using our ATM. You can leave.")
            break
        else:
            print("Invalid choice. Choose from 1-4")

atmSimulator()