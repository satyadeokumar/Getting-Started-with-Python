Text = " This is a python string"
x = Text.find("python")
y = Text.find("is")
z = Text.find("e", 5)

print(x)
print(y)
print(z)

word = "python is a programming language"
letter = "a"
position = word.find(letter) # returns 2 (0-based index)
if position != -1:
   print(f"'{letter}' found at index {position}")
else:
   print(f"'{letter}' not found")