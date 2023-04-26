#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.
import pyperclip
text_list= []

def n_articles():
    while True:
        
        while True:
            try:
                n = int(input("Enter the size of Wikipedia article: "))
                break
            except ValueError:
                print("Not an integer! Try again.")
                
        for i in range(1, n+1):
            print("yo need to specify the article topic \n Listo of <<article here>>")
            print("Wikipedia article number:", i, )
            item = input("List of ")
            text_list.append(item)
        print("the info saved is: ",text_list)
        break 
    
def stars():
    for i in range (len(text_list)):
        print(" * List of ",text_list[i])
        
""" 
    #! python3
    # bulletPointAdder.py - Adds Wikipedia bullet points to the start
    # of each line of text on the clipboard.
    import pyperclip
    text = pyperclip.paste()
    
    # Separate lines and add stars.
    lines = text.split('\n')
    for i in range(len(lines)): # loop through all indexes for "lines" list
        lines[i] = '* ' + lines[i] # add star to each string in "lines" list
    text = '\n'.join(lines)
    pyperclip.copy(text)
    ------------------------------
    This is the code that the book gave me ass answer.
    
    By myself I create a list 
    where the number of articles are going to be stored in a for cicle, validating 
    that the number of articles are going to be created is a number, then show the number of article
    you are creating, the the name of the artible and finishing the cicle when you reach the number of articles 
    you give 
    then the articles are deployed at the screen. 
    
"""
      
n_articles()
stars()    
    
    