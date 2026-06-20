# Python has multiple arithmetic operations for calculations

""""
Operator	Description
+	        Addition
-	        Subtraction
*	        Multiplication
/	        Division (float)
//	        Floor Division
%	        Modulus (remainder)
**	        Exponentiation

Built-in math Module Functions - provides extra math capabilities.

import math

# Basic math functions
print(math.sqrt(16))       # Square root → 4.0
print(math.pow(2, 3))      # Power → 8.0
print(math.factorial(5))   # Factorial → 120
print(math.gcd(12, 18))    # Greatest Common Divisor → 6

# Rounding functions
print(math.ceil(4.3))      # Round up → 5
print(math.floor(4.7))     # Round down → 4

# Constants
print(math.pi)             # 3.141592653589793
print(math.e)              # 2.718281828459045
"""
# A few examples
num1 = 5
num2 = 10

addition = num1 + num2
subtraction = num2 - num1
multiplication = num1 * num2
division = num2 / num1
floor_division = num2 // num1
modulus = num2 % num1
power = num1 ** num2

print("Sum of both numbers is:", addition)
print("Difference of the numbers is:", subtraction)
print("Multiplication of the numbers is:", multiplication)
print("Division of number 2 by number 1 is:", division)
print("Floor division of number 2 by number 1 is:", floor_division)
print("Remainder when dividing number 2 by number 1 is:", modulus)
print("num1 raised to the power of num2 is:", power)

# Extra math examples using the built-in math module
import math

print("Square root of 16 is:", math.sqrt(16))
print("2 to the power of 3 is:", math.pow(2, 3))
print("Factorial of 5 is:", math.factorial(5))
print("GCD of 12 and 18 is:", math.gcd(12, 18))
print("Rounded up value of 4.3 is:", math.ceil(4.3))
print("Rounded down value of 4.7 is:", math.floor(4.7))
print("Value of pi is:", math.pi)
print("Value of e is:", math.e)