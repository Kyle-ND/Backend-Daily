#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

from docx import Document
import os

print("Current Working Directory:", os.getcwd())

#Creating paths to all the files and folders I will use in this project
names_path = "Input/Names/inivited_names.txt"
letter_path = "Input/letters/starting_letter.docx"
output_path = "Output/ReadyToSend"

#Checking if the output diretory exist
os.makedirs(output_path, exist_ok=True)

#Opening the names file and reading it 
with open(names_path, "r") as names_file:
    names = names_file.readlines()


#loading the letter 
letter_template = Document(letter_path)

for name in names:         #Removing any leading/trailing whitespace
    name = name.strip()
    new_letter = Document   #Create a new document for each name

    for paragraph in letter_template.paragraph:
        new_paragraph = new_letter.add_paragraph(paragraph.text.replace("[name]", name))

#Saving the letter in the RedayToSend Folder
    new_letter.save(f"{output_path}/letter_for_{name}.docx")
