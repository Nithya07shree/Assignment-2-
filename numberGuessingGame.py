import random

bestScore = None

while True:
    secret = random.randint(1,100)
    attemptsUsed = 0
    attemptsRemaining = 10
    won = False
    
    print("\n"+"="*45)
    print("This is a guessing game.")
    print(f"Find the number I chose between 1-100. You have {attemptsRemaining} tries.")
    
    if bestScore is not None:
        print(f"Current best score: {bestScore} attempts")
    print("="*45)
    
    while attemptsUsed<attemptsRemaining:
        guess = input("Enter guess :")
        if guess.isdigit():
            guess = int(guess)
            attemptsUsed+=1
        else:
            print("Invalid input!. Enter a whole number !!")
            continue
        
        if guess == secret:
            print(f"Yay!! You guessed it right in {attemptsUsed} attempts.")
            won = True
            if bestScore is None or attemptsUsed<bestScore:
                bestScore = attemptsUsed
                print("New best score!!")
            break
        
        if abs(guess-secret)<=5:
            print("HINT: You are very close(within 5 units)")
        
        if guess<secret:
            print(f"Too low. {attemptsRemaining-attemptsUsed} attempts remaining.")
        else:
            print(f"Too high. {attemptsRemaining-attemptsUsed} attempts remaining.")
        
    if not won:
        print(f"You did not guess in 10 attempts failure. The number was {secret}. ")
    
    flag = input(" Wanna play again? (y/n):").lower()
    if flag!="y":
        print(f"You played well! This is your best score: {bestScore}")
        break