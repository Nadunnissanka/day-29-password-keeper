# Handling Errors and exceptions - refer 100 days of code challenge - Lecture 268
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed!")
