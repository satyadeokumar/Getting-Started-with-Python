import math

#Taking input for start of range
m=int(input("Enter start of range: "))

#Taking input for end of range
n=int(input("Enter end of range: "))

print("Given range is:", m, "to", n)
print("The numbers in given range with all digits even are: ")

arr=[]      #Creating an empty list
for i in range(m, n + 1):      # Setting a for loop from m to n
    num = abs(i)           # Use absolute value to handle negative numbers
    isValid = True          # Setting a boolean variable to True
    # Extract each digit of num and check if it is even

    if num == 0:
        arr.append(i)
        continue

    while num != 0:
        digit = num % 10   # Extracting digit
        num //= 10
        if digit % 2 != 0:     # Checking if digit is odd
            isValid = False   # If odd, then isValid is set to False
            break       # Breaking loop if odd digit found
    if isValid:        # If isValid remains True, then all digits are even
        arr.append(i)
print(arr)      # Printing the list