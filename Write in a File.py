"""
Mode / Option	description
"r"	Read mode: default mode, file must exist
"w"	Write mode: creates file if missing, truncates (erases) if it exists
"a"	Append mode: creates file if missing, writes data always at the end
"x"	Exclusive create: creates new file, but fails with FileExistsError if it already exists
"b"	Binary flag: used with other modes (e.g., "wb", "ab") for binary files
"+"	Read/write flag: combine with other modes (e.g., "r+", "w+") for both reading and writing
encoding=	Specify text encoding (e.g., "utf-8") when working with text files
newline=	Control newline translation in text mode (e.g., "\n")


"""



with open("Dummyfile.txt", "w", encoding="utf-8") as f:
    f.write("This file is Created using write mode.\n")
    f.write("Add Second line.\n")

with open("Dummyfile.txt", "r", encoding="utf-8") as f:
    print(f.read())

with open("Dummyfile.txt", "a", encoding="utf-8") as f:
    f.write("Appended line in dummy file.\n")

with open("Dummyfile.txt", "r", encoding="utf-8") as f:
    print(f.read())

