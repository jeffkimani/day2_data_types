#A program that calculates tips and splits bills
print("Welcome to the tip calculator")
#user bill
bill = input("Enter total bill: $")
converted_bill = float(bill)
#percentage tip
percentage_tip = input("What percentage tip would you like to give: 10%, 12%, or 15%? ")
tip = int(percentage_tip)/100 * converted_bill
#Split
number_of_people = input("How many people are splitting the bill: ")
converted_people = int(number_of_people)
#Calculation
total_bill = float((converted_bill + tip)/converted_people)
#total Bill
print (f"The total bill to be paid is {total_bill}")

#the debugged file# Jeffrey the DON!!