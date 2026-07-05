# Open the file in read mode
file = open(r"C:\devhome\Github\Getting-Started-with-Python\ExampleFile.txt", "r")

# Read the entire content of the file
content = file.read()
print(content)

# Close the file
file.close()

# Reading the line line by line
file = open(r"C:\devhome\Github\Getting-Started-with-Python\ExampleFile.txt", "r")
for line in file:
    print(line.strip())  # .strip() to remove newline characters
file.close()

file = open(r"C:\devhome\Github\Getting-Started-with-Python\ExampleFile.txt", "r")
line = file.readline()
while line:
    print(line.strip())
    line = file.readline()
file.close()

file = open(r"C:\devhome\Github\Getting-Started-with-Python\ExampleFile.txt", "r")
content = file.read(10)
print(content)
file.close()