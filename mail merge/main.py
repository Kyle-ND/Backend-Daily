import os


def main():
    try:
        # Open the 'invited_names.txt' file and read all names
        with open("./Input/Names/inivited_names.txt") as data:
            names = [name.strip() for name in data]
    except FileNotFoundError:
        # If the 'invited_names.txt' file is not found, raise an error
        raise FileNotFoundError('Check if the file path is correct.')

    try:
        # Open the 'starting_letter.docx' file for reading
        with open('./Input/letters/starting_letter.docx') as data:
            template = data.readlines()
    except FileNotFoundError:
        # If the 'starting_letter.docx' file is not found, raise an error
        raise FileNotFoundError('Check if the file path is correct.')

    # Loop through the list of names
    for i, name in enumerate(names):
        # Join all lines from the template into a single string
        letter = "".join(template)

        # Replace the [name] placeholder with the actual name
        letter = letter.replace("[name]", name)


        # Ensure the 'ReadyToSend' directory exists
        if not os.path.exists('ReadyToSend'):
            os.makedirs('ReadyToSend')

        # Open a new text file to save the personalized letter for each name
        with open(f"ReadyToSend/{name}'s letter.txt", 'a') as contents:
            # Write the personalized letter to the file
            contents.write(f"{letter}")


# Entry point of the program
if __name__ == "__main__":
    main()
