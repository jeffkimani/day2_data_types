#A program that calculates tips and splits bills
print("Welcome to the tip calculator")
#user bill
user_bill = input("What is the total bill: $")
#percentage tip
percentage_tip = input("What percentage tip would you like to give?")
#number of bill payers:
people_bill = input("How many people should split the bill? ")
bill_with_tip = int((percentage_tip)/100) * float((round(user_bill, 2))) + float((round(user_bill, 2)))

print(bill_with_tip)

#logical & syntax error --- will debug tomorrow