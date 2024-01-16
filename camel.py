camelCase = input("camelCase: ")
for letter in camelCase:

    if letter.isupper():
        print("_" + letter.lower(), end="")

    else:
        print(letter, end="")


