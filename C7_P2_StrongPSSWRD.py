"""
Write a function that uses regular expressions to make sure the password
string it is passed is strong. A strong password is defined as one that
is at least eight characters long, contains both uppercase and lowercase
characters, and has at least one digit. You may need to test the string
against multiple regex patterns to validate its strength.

1) at least 8 characters
2) at least one upper case
3) at least one lower case
4) at least one number

"""
import re

def UserPsswrd():
    while True:
        RegexPsswrd=re.compile(r'''(
        ^(?=.*[A-Z].*[A-Z])                #DOS MAYUSCULAS/CAPITAL LETTERS
        (?=.*[!@#$&*])                     # DOS CARACTERES ESPECIALES/TWO ESPECIAL CHARACTERS
        (?=.*[0-9].*[0-9])                 # DOS DIGITOS/TWO DIGITS
        (?=.*[a-z].*[a-z].*[a-z])          # MINIMO 3 LETRAS MINUSCILAS/ AT LEAST 3 LOWERCASE LETTERS
        .{10,}                             #DIEZ DIGITOS MINIMOS TOTALES/ AL LEAST 10 TOTAL CHARACTERS
        $
        )''', re.VERBOSE)
        password=input("Enter the ne password: ")
        check=RegexPsswrd.search(password)
        if (not check):
            print("Your password it's not strong enough...")
        else:
            print("Your password its strong enough...for now ")
            
            
UserPsswrd()
        