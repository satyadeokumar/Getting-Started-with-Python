# Temperature input in Celsius
celsius = float(input("Enter temperature in Celsius: "))
# Convert to Fahrenheit using the formula
fahrenheit = (celsius * 9/5) + 32
# Display result with 2 decimal places
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")