# Python has multiple arithmetic operations for calculations

"""
Operator    Description
+           Addition
-           Subtraction
*           Multiplication
/           Division (float)
//          Floor Division
%           Modulus (remainder)
**          Exponentiation
"""

# Basic arithmetic examples
num1 = 5
num2 = 10
num3 = 3

addition = num1 + num2
subtraction = num2 - num1
multiplication = num1 * num2
division = num2 / num1
floor_division = num2 // num1
modulus = num2 % num1
power = num1 ** num3

print("\nBasic arithmetic operations")
print("Sum of both numbers is:", addition)
print("Difference of the numbers is:", subtraction)
print("Multiplication of the numbers is:", multiplication)
print("Division of number 2 by number 1 is:", division)
print("Floor division of number 2 by number 1 is:", floor_division)
print("Remainder when dividing number 2 by number 1 is:", modulus)
print("num1 raised to the power of num3 is:", power)

# More arithmetic examples
average = (num1 + num2 + num3) / 3
percentage = (num1 / num2) * 100
square = num2 ** 2
cube = num3 ** 3
combined = (num1 * num2) + (num3 ** 2) - (num2 // num1)

print("\nMore arithmetic examples")
print("Average of the three numbers is:", average)
print("Percentage of num1 out of num2 is:", percentage, "%")
print("Square of num2 is:", square)
print("Cube of num3 is:", cube)
print("Combined expression result is:", combined)

# Extra examples with decimals
price = 19.99
discount = 0.10
discounted_price = price - (price * discount)

print("\nDecimal examples")
print("Original price:", price)
print("Discounted price:", discounted_price)

# Extra math examples using the built-in math module
import math

print("\nUsing the math module")
print("Square root of 16 is:", math.sqrt(16))
print("2 to the power of 3 is:", math.pow(2, 3))
print("Factorial of 5 is:", math.factorial(5))
print("GCD of 12 and 18 is:", math.gcd(12, 18))
print("Rounded up value of 4.3 is:", math.ceil(4.3))
print("Rounded down value of 4.7 is:", math.floor(4.7))
print("Value of pi is:", math.pi)
print("Value of e is:", math.e)