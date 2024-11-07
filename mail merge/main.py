import os


def read_names(path):
    #opening the name file
    with open(path, "r") as invites:
        lines = invites.readlines()
        name_lst = []
        for names in lines:
            name = names.strip()
            name_lst.append(name)
    return name_lst

def read_letters(doc_path):
    #Opening the docx file
    with open(doc_path, "r") as greet:
        return greet.read()

def main():
    #The path of the file for the inivited_name.txt.
    path = r"C:\Users\makho\Documents\My_projects\Backend-Daily\mail merge\Input\Names\inivited_names.txt"
    #Path for the docx file.
    doc_path = r"C:\Users\makho\Documents\My_projects\Backend-Daily\mail merge\Input\letters\starting_letter.docx"
    #The folder for ready letters
    outbox = r"C:\Users\makho\Documents\My_projects\Backend-Daily\mail merge\ReadyToSend"

    names = read_names(path)
    greet = read_letters(doc_path)

    for name in names:
        greetings = greet.replace("[name]", name)
        mails_ = (f"{name} ready_to_send.docx")
        outbox_path = os.path.join(outbox,mails_)

    with open(outbox_path, 'w') as sent_mail:
        sent_mail.write(greetings)
            
    print(f"Files are saved on the {mails_} file, on {outbox_path} path")
main()


#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
