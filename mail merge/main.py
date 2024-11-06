def main():
    #The path of the file for the inivited_name.txt.
    path = r"C:\Users\makho\Documents\My_projects\Backend-Daily\mail merge\Input\Names\inivited_names.txt"
    #Path for the docx file.
    doc_path = r"C:\Users\makho\Documents\My_projects\Backend-Daily\mail merge\Input\letters\starting_letter.docx"
    #The folder for ready letters
    outbox = r"C:\Users\makho\Documents\My_projects\Backend-Daily\mail merge\ReadyToSend"

    #opening the name file
    invites = open(path, "r").readlines()
    #Opening the docx file
    greet = open(doc_path, "r").read()
    print(greet)

    for names in invites:
        name = names.strip()
        greetings = greet.replace("[name]",name)
        print(greetings) 
main()


#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
