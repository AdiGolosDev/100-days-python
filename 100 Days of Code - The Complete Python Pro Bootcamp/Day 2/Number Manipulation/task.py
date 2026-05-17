weight = int(input("Please input your weight: "))
height = float(input("Please input your height(floating point number): "))

bmi = weight / height ** 2

print(f"Your BMI is: {bmi:.2f}")