# get input from users
age = int(input("Enter the age of person: "))
dayOfWeek = input("Enter the day of week: ")
numberOfTickets = int(input("Enter the number of tickets required: "))

# age logic
if age<3:
    price = 0
    category = "Free"
elif 3<=age<=12:
    price = 150
    category = "Child"
elif 13<=age<=59:
    price = 300
    category = "Adult"
else:
    price = 200
    category = "Senior"

# day based logic
if dayOfWeek in ["Friday", "Saturday", "Sunday"]:
    discountPercent = 20
else:
    discountPercent = 0
    
# Calculate total amount
discountPrice = (price*discountPercent)/100
pricePerTicket = price-discountPrice
totalAmount = pricePerTicket*numberOfTickets

# print result
print(f"========Ticket ({category})========")
print(f"Base price        : Rs.{price}")
print(f"Day               : {dayOfWeek}")
print(f"Discount ({discountPercent}%)    : Rs.{discountPrice}")
print(f"Price Per Ticket  : Rs.{pricePerTicket}")
print(f"Number of tickets : {numberOfTickets}")
print("="*30)
print(f"Total Amount      : Rs.{totalAmount}")