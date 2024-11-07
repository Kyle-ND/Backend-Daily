# TODO: Create a letter using starting_letter.docx
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".


# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
def letter_file():
    with open("./Input/letters/starting_letter.docx", "r") as file:

        lines = file.readlines()
        return lines


def names_file():
    names = []
    f = open("./Input/Names/inivited_names.txt", "r")
    contents = f.readlines()
    for line in contents:
        names.append(line.strip())

    return names


def construct_letter():
    names = names_file()
    lex = letter_file()
    letterx = "".join(lex)
    new_letter = ""
    for name in names:
        new_letter = letterx.replace("[name]", name)

        with open(f"./Input/ReadyToSend/{name}.docx", "w") as file:
            file.write(new_letter)


construct_letter()
