#Question 1 
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time period (in years): "))


simple_interest = (principal * rate * time) / 100

print("The simple interest is: ", simple_interest)

#Question 2


celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")

#Question 3

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
perimeter = 2 * (length + width)
print(f"Area: {area} square units")
print(f"Perimeter: {perimeter} units")

#Question 4

char = input("Enter a character: ")
ascii_value = ord(char)
print(f"The ASCII value of '{char}' is {ascii_value}")

#Question 5
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius
print(f"Area: {area:.2f} square units")
print(f"Circumference: {circumference:.2f} units")

#Question 6
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num1, num2 = num2, num1

print(f"Swapped numbers: {num1}, {num2}")

#Question 7 
import math
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"The roots are real and distinct: {root1}, {root2}")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"The roots are real and equal: {root}")
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-discriminant) / (2*a)
    print(f"The roots are complex: {real_part} + {imaginary_part}i, {real_part} - {imaginary_part}i")

#Question 8
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You are normal weight.")
elif bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")


