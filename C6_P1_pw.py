#! python3
# P1_pw.py - An insecure password locker program.


PASSWORDS = {'email': '123456', 'tw': 'abcdef', 'ig': '123abc'}

import sys,pyperclip
#this library This module provides access to some variables used or maintained 
#by the interpreter and to functions that interact strongly with the interpreter.


if len(sys.argv) < 2:
    print("Usage: python C6_P1_pw.py [account] - copy account password")
    sys.exit()

account=sys.argv[1]
 
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)