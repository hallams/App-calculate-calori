
#This Python script calculates the Basal Metabolic Rate (BMR) and daily calorie needs
#based on user inputs for weight, height, age, gender, and activity level.
import json



# Read data from the "userdata.json" file
with open("userdata.json", "r") as file:
    data = json.load(file)

# Extract information for a specific member (e.g., 'Halla')
username = input("Enter your name please : ")

# Convert username to lowercase for case-insensitive matching
member_info = data.get(username.lower())
if member_info is None:
    print("name not found.")
else:
    weight_kg = float(member_info['weight'])  # Convert weight to float
    height_cm = float(member_info['height'])  # Convert height to float
    age_years = int(member_info['age'])  # Convert age to int
    gender_input = member_info['gender']
    active_input = member_info['activity_level']

    def calculate_bmr(weight, height, age, gender):
        if gender.lower() == 'male':
            bmr = 66.47 + (13.7 * weight) + (5 * height) - (6.8 * age)
        elif gender.lower() == 'female':
            bmr = 655.1 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
        else:
            print("Invalid gender specified. Please enter 'male' or 'female'.")
            return None  # Return None if gender is invalid
        return bmr

    bmr_result = calculate_bmr(weight_kg, height_cm, age_years, gender_input)
    if bmr_result is not None:
        print(f" (BMR) is: {bmr_result} ")

        # Code for calorie calculation
        def calculate_calorie_needs(bmr, activity_level):
            activity_multipliers = {
                'l active': 1.375,
                'm active': 1.55,
                'v active': 1.725,
            }

            if activity_level.lower() not in activity_multipliers:
                raise ValueError("Invalid activity level specified.")

            activity_multiplier = activity_multipliers[activity_level.lower()]
            calorie_result = bmr * activity_multiplier  # Calculate calories based on BMR and activity level
            return calorie_result

        

        calorie_result = calculate_calorie_needs(bmr_result, active_input)
        print(f"Your daily calorie needs are: {calorie_result} calories.")
        user_info = {
            'BMR': bmr_result,
            'calorie_needs': calorie_result
        }

        with open("user_info.json", "w") as file:
            json.dump(user_info, file)
