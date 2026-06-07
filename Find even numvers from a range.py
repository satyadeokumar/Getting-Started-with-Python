import math

#Taking input for start of range
m=int(input("Enter start of range: "))

#Taking input for end of range
n=int(input("Enter end of range: "))

print("Given range is:", m, "to", n)
print("The even numbers in the given range are:")

arr=[]      # Creating an empty list
for i in range(m, n + 1):      # Setting a for loop from m to n
    if i % 2 == 0:             # Check if the number itself is even
        arr.append(i)
print(arr)      # Printing the list