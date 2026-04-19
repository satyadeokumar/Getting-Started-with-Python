import math

#Write a program that accepts a sentence and calculate the number of letters and digits
s = input("Input a string")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("LETTERS", l)
print("DIGITS:", d)