#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def read_txt_file():
    f = open("./Input/Names/invited_names.txt", "r")

    content = f.readlines()
    new_names = [name.strip() for name in content]

    return new_names

def read_docx_file():
    n = read_txt_file()

    page = open("./Input/letters/starting_letter.docx")

    letter = page.readlines()

    clean_letter = [let.strip() for let in letter]
    
    new_letter = []
    
    for i in n:
        for j in clean_letter:
            if j == 'Dear [name],':
                j = j.replace('Dear [name],', f'Dear {i}')
                new_letter.append(j)
            else:
                new_letter.append(j)

    return new_letter

def write_to_txt():
    x = read_docx_file()
    
    with open(r"./ready_to_send/send.txt", 'w') as fp:
        for letter in x:
            fp.write("%s\n" % letter)
    print('Done')


write_to_txt()


    


