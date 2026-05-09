# BMI Calculator

# Ask the user for weight in kilograms
weight = float(input("Enter your weight (kg): "))

# Ask the user for height in meters
height = float(input("Enter your height (m): "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display BMI result
print(f"\nYour BMI is: {bmi:.2f}")

# Provide health advice based on BMI
if bmi < 18.5:
    print("Health Advice: You are underweight. Consider a balanced diet and healthy weight gain.")
elif bmi < 25:
    print("Health Advice: You are in the normal weight range. Keep maintaining a healthy lifestyle!")
elif bmi < 30:
    print("Health Advice: You are overweight. Regular exercise and healthy eating are recommended.")
else:
    print("Health Advice: You are in the obesity range. Consider consulting a healthcare professional.")