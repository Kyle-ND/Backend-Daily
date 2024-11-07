#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
letter_path = 'Input/letters/starting_letter.docx'
invited_names_path = 'Input/Names/inivited_names.txt'
def read_starting_letter(filename):
    try:
        with open (filename) as file:
            letter_contents = file.read()
        return letter_contents
    except FileNotFoundError:
        print("File not found")
def read_invited_names(path_to_file):
    try:
        with open(path_to_file) as f:
            f_contents = f.read().split('\n')
        return f_contents
    except FileNotFoundError:
        print('File not found')
#print(read_invited_names(invited_names_path))
def create_letter(letter_structure,recipients):
    save_to_path = 'ReadyToSend/'
    if recipients:
        for name in recipients:
            new_letter = letter_structure.replace('[name]',name)
            name_of_new_file = f"{save_to_path}{name}_letter.docx"
            try:
                with open(name_of_new_file,'w') as file_object:
                    file_object.write(new_letter)
                print(f"You have successfuly written a letter to {name}")
            except FileNotFoundError:
                print("File not found")
    else:
        print("List of recipients is empty.")

#if __name__ == '__main__)':
create_letter(read_starting_letter(letter_path),read_invited_names(invited_names_path))



