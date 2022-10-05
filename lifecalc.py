#A program that calculates how many years, weeks, and days I have left in my life if I am lucky enough to reach 90 years old

#user input
user_age = input("How old are you: ")

#conversion & calculation
#check the calculation --- I'm not sure if it is entirely correct
years_left = 90 - int(user_age)
weeks_left = years_left * 52
days_left = years_left * 365

print(f"You have {years_left} years, {weeks_left} weeks, and {days_left} days left in your life")