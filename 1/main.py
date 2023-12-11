# import pandas as pd
#
#
# #lists and data types
# my_list = ['apple', 'oranges', 2, 4,3 ]
#
# print(len(my_list))
#
# my_list.pop(3)
# print(my_list)
#
# userAge = [21, 23 ,25, 27]


# def get_bmi(height, weight):
#     return weight / (height * height)
#
# height_input = input("Enter your height: ")
# weight_input = input("Enter your weight: ")
#
# bmi = get_bmi(float(height_input), float(weight_input))
# print(f'your BMI is: {bmi}')
#
#
## Do the tip calculator here
#
# bill_total = input("What is the total for the bill? ")
# tip_percentage = input("What percentage would you like to tip? ")
# people_count = input("How many people are splitting the bill? ")
# total_with_tip = (int(bill_total) + int(bill_total) *  int(tip_percentage) / 100) / int(people_count)
#
# print(f"Your total is: {bill_total}, if you want to tip {tip_percentage}%, then total will be: {total_with_tip}$, for {people_count} people.")

print("Add a number you want to add! for example 12 is 13!")

numbers = input("Input number now ....")

sum_numbers = int(numbers[0]) + int(numbers[1])
print(f"Your number is: {sum_numbers}")

print(type(sum_numbers))