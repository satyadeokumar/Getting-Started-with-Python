#Write a code which accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically

# take input from the user
my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = my_str.split()

# sort the list
words.sort()

# display the sorted words
for word in words:
    print(word)