""" 
Write a function named printTable() that takes a list of lists of strings
and displays it in a well-organized table with each column right-justified.
Assume that all the inner lists will contain the same number of strings.
For example, the value could look like this:

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

Your printTable() function would print the following:
apples Alice dogs
oranges Bob cats
cherries Carol moose
banana David goose

"""

def printTable(table):
    col_widths = LongestWord(table)
    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i].rjust(col_widths[j]), end=' ')
        print()


def LongestWord(table):
    return[max([len(item) for item in line]) for line in table]



def menu():
    while True:
        while True:
            try:
                print("How do you want to see the table?")
                print('''
                    ----SELECT A NUMBER----
                    1 for disorganized
                    2 for organized
                    0 for exit
                    ''')
                o=int(input('How doy you want to see the table?'))
                break
            except ValueError:
                print("Not an integer! Try again.")
        if o== 1:
            print(TableData)
            print("\n")
            input("<<ENTER TO COTINUE>>")
            print("\n")
        elif o==2:
            printTable(TableData)
            print("\n")
            input("<<ENTER TO COTINUE>>")
            print("\n")
        else:
            print("closing program...")
            break
    

TableData=[['apples', 'oranges','cherries','banana'],
           ['Alice','Bob','Carol','David'],
           ['dogs','cats','mouse','goose']]

menu()
