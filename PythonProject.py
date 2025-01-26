def calculate_bmi(weight, height):
  return weight / (height ** 2)

def get_bmi_category(bmi):
  if bmi < 18.5:
    return "Underweight"
  elif 18.5 <= bmi < 25:
    return "Normal"
  elif 25 <= bmi < 30:
    return "Overweight"
  else:
    return "Obese"

# Get user input
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = calculate_bmi(weight, height)

# Determine BMI category
category = get_bmi_category(bmi)

# Print results
print(f"Your BMI is: {bmi:.2f}")
print(f"BMI Category: {category}")