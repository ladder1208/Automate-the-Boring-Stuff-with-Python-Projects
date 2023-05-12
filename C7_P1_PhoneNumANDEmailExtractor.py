# Project: Phone number and email Address extractor
# Automate the Boring Stuff With Python

import pyperclip, re
info= str(pyperclip.paste())

# create phone number regex
def RegexPhone():
    phoneRegex=re.compile(r'''(
    (\d{3}|\(\d{3}\))?             # area code
    (\s|-|\.)?                     # separator
    (\d{3})                        # first 3 digits
    (\s|-|\.)                      # separator
    (\d{4})                        # last 4 digits
    )''', re.VERBOSE)
    # num=phoneRegex.findall(info)
    # print(num)
    for num in phoneRegex.findall(info):
        print(num)


def RegexEmail():
    emailRegex= re.compile(r'''
    [a-zA-Z0-9.+_-]+  #username
    @                 #@ character
    [a-zA-Z0-9.+_-]+  #domain name
    \.[a-zA-Z]        #. 
    [a-zA-Z]*         #after the . ".something"
    ''',re.VERBOSE)
    for mail in emailRegex.findall(info):
        print(mail)


def main():
    RegexPhone()
    RegexEmail()
    
main()