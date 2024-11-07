#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import os

#Define directory and file paths
invited_names_path = os.path.abspath('mail merge/Names/inivited_names.txt')
starting_letter_path = os.path.abspath('mail merge/letters/starting_letter.docx')
ready_path = os.path.abspath('ReadyToSend')


# Ensure the ReadyToSend directory exists
os.makedirs(ready_path, exist_ok=True)

# Populate array with names 
with open(invited_names_path, mode='r') as file:
    names = [line.strip() for line in file.readlines()]

# Read the starting contents
with open(starting_letter_path, mode='r') as starting_file:
    starting_content = starting_file.read()

# Create personalized letters by modifying starting_contents and write to new file
for name in names:
    modified_letter_path = os.path.join(ready_path, f'{name}.docx')
    modified_content = starting_content.replace('[name]', name)

    # Write the modified content to a new file
    with open(modified_letter_path, mode='w') as file:
        file.write(modified_content)
             


