with open("Dummyfile.txt", "w", encoding="utf-8") as f:
    f.write("This file is Created using write mode.\n")
    f.write("Add Second line.\n")

with open("Dummyfile.txt", "r", encoding="utf-8") as f:
    print(f.read())

with open("Dummyfile.txt", "a", encoding="utf-8") as f:
    f.write("Appended line in dummy file.\n")

with open("Dummyfile.txt", "r", encoding="utf-8") as f:
    print(f.read())

