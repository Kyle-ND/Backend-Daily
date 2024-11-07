#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import os

# Define directory and file paths
# dir_name = '/home/wtc/Documents/RepositoryAccounts/Backend-Daily/mail merge'
# invited_names_path = os.path.join(dir_name, 'Names/invited_names.txt')
# starting_letter_path = os.path.join(dir_name, 'letters/starting_letter.docx')
# ready_path = os.path.join(dir_name, 'ReadyToSend')

invited_names_path = '/home/wtc/Documents/RepositoryAccounts/Backend-Daily/mail merge/Names/inivited_names.txt'
starting_letter_path = '/home/wtc/Documents/RepositoryAccounts/Backend-Daily/mail merge/letters/starting_letter.docx'
ready_path = '/home/wtc/Documents/RepositoryAccounts/Backend-Daily/mail merge/ReadyToSend'


os.makedirs(ready_path, exist_ok=True)

# Populate array with names that are invited
with open(invited_names_path, mode='r') as file:
    names = [line.strip() for line in file.readlines()]

# Get the contents of the letter template
with open(starting_letter_path, mode='r') as starting_file:
    starting_content = starting_file.read()

# Modify the content of letter template, and write to a new file
for name in names:
    modified_content = starting_content.replace('[name]', name)
    modified_letter_path = os.path.join(ready_path, f'{name}.docx')

    with open(modified_letter_path, mode='w') as file:
        file.write(modified_content)

             


