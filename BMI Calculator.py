#i am adding the input field here
weight = int(input("Enter Weight (KG) : "))
height = float(input("Enter Height (Meters) : "))

#calculating for BMI now

bmi_cal = weight / (height ** 2)

#rounding of value to 3 significant figures

bmi = f"{bmi_cal:.3g}"

print("Your BMI Is: ",bmi)

#printing BMI

print("Check Your BMI Categories Below:")

#adding categories for user to know where their BMI result falls

bmi_categories = [" Underweight: Below 18.5", "Healthy weight: 18.5 to 24.9", "Overweight: 25.0 to 29.9", "Obesity: 30.0 or greater"]

print(bmi_categories)
