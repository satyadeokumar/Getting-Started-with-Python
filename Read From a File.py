# Open the file in read mode
file = open(r"C:\devhome\Github\Getting-Started-with-Python\ExampleFile.txt", "r")

# Read the entire content of the file
content = file.read()
print(content)

# Close the file
file.close()

