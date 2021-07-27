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

# Example 01
fruits = ["Apple", "Pear", "Orange"]


# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " pie")
    except IndexError:
        print("fruit pie")


make_pie(4)
