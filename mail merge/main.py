#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
def names_file():
    with open("./Input/Names/inivited_names.txt", "r") as file:
        lines = file.readlines()
    names = []
    for line in lines:
        clean = line.strip()
        names.append(clean)
    return names

def letter(names):
    with open("./Input/letters/starting_letter.docx", "r") as file:
        content = file.read()
    for name in names:
        if "[name]" in content:
            content = content.replace("[name]",name)
        # if name in content:
        #     content = content.replace(name,names)
    print(content)
    
            
letter(names_file())