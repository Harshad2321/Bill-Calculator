print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
b=bill*(tip/100)+bill
pay=round((b/people),2)
print("Each person should pay: $",pay)
