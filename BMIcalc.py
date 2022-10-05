#BMI calculator
#Formula = weight (in kgs)/heigt ** height
#Convert the value to a whole number

#Request user input => weight (kgs) & height:
user_weight = input("Please enter your weight(kgs): ")
user_height = input("Please enter your height(m): ")
#BMI formula
BMI = int(user_weight) / float(user_height) ** 2
#print user BMI
print(f"Your Body Mass Index is: {int(round(BMI))}")