import math

#Taking input for start of range
m=int(input("Enter value of m: "))

#Taking input for end of range
n=int(input("Enter value of n: "))

print("Given range is:", m, "to", n)
print("The numbers in given range with all digits even are: ")


arr=[]      #Creating an empty list

for i in range(m,n+1):      #Setting a for loop from m to n

    num=i           #Taking a variable num to work upon

    isValid=True    #Setting a boolean variable to True

    #Extract each digit of num and check if it is even

    while(num!=0):

        digit=num%10   #Extracting digit

        num=num//10

        if(digit%2!=0):     #Checking if digit is odd

            isValid=False   #If odd, then isValid is set to False

            break       #Breaking loop if odd digit found


    if(isValid):        #If isValid remains True, then all digits are even

        arr.append(i)


print(arr)      #Printing the list