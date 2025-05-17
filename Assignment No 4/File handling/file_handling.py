# 1. Writing to a file (creates if not exists, overwrites if exists)
with open("sample.txt", "w") as file:
    file.write("Hello, this is the first line.\n")
    file.write("File handling in Python is easy!\n")

# 2. Reading the file
with open("sample.txt", "r") as file:
    print("📖 Reading file contents:")
    content = file.read()
    print(content)

# 3. Appending to the same file
with open("sample.txt", "a") as file:
    file.write("This line was appended later.\n")

# 4. Reading again to show updated content
with open("sample.txt", "r") as file:
    print("📖 Updated file contents:")
    print(file.read())
