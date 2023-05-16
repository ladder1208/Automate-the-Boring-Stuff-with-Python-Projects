""" 
Create a Mad Libs program that reads in text files and lets the user add
their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
appears in the text file. For example, a text file may look like this:

The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.

The program would find these occurrences and prompt the user to
replace them.
Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck

The following text file would then be created:
The silly panda walked to the chandelier and then screamed. A nearby pickup
truck was unaffected by these events.
The results should be printed to the screen and saved to a new text file.
"""

import re                            #while using regex we need the re library

def WordsChange():                   #define the fuction
    global text                      # text is global because is usen in differents fuctions
    file=open('test.txt')            #open the file, give the file a variable where its going to be manipulated
    text=file.read()                 
    print("\n")
    print(text)                      #show what does the contina
    print('\n')
    file.close()
    regex=re.compile(r'(ADJECTIVE)|(NOUN)|(VERB)')   #declare whats does regex is looking for
    for i in regex.findall(text):                    #ussing findall matches all the similitudes and save it in i
        for j in i:                                  #extracts the matches individually 
            if j!='':                                #ignores that not matches with the regex
                reg=re.compile(r'{}'.format(j))
                usrwords=input('Enter the substitute for "%s" TO: ' %j)
                text=reg.sub(usrwords,text,1) #number 1 limits de n of changes
            

def main():
    WordsChange()         #previous function
    print('\n')
    print(text)          #show how does the new text looks
    file=open('test.txt','w')
    file.write(text)     #open the file, write the new next and close it.
    file.close()

main()