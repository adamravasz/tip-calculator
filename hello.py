print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? £"))

tip = int(input("What percentage tip would you like to give?  "))

guests = int(input("How many people are splitting the bill? " ))

tip_percent = tip / 100 

tip_amount = bill * tip_percent

total_bill = bill + tip_amount

bill_per_person = total_bill / guests 

final = round(bill_per_person, 2) 

final = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: £{final}")