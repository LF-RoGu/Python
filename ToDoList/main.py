# Author: Luis Fernando Rodriguez Gutierrez
# Institution: FH-Dortmund
# Program: ESE

# Imports
from enum import Enum


class enum_userOptions(Enum):
    Add = 1
    Show = 2
    Edit = 3
    Exit = 5


class class_PersonInfo:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def funct_userOptionString(varString):
    # No matter how the string arrives, all string to upper case
    varString.upper()

    match varString:
        case 'ADD':
            return enum_userOptions.Add.value
        case 'SHOW':
            return enum_userOptions.Show.value
        case 'EDIT':
            return enum_userOptions.Edit.value
        case 'EXIT':
            return enum_userOptions.Exit.value
    # Return Null
    return None

def funct_showListItems(varList):
    print("Items in the list... ")
    if not var_listToDo:
        print("[!] List is empty")
    else:
        for index, item in enumerate(var_listToDo):
            # Plus 1 added to avoid index 0 in the list when showing the item
            print(f"{index+1}. {item} \n")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Create all the possible variables that are going to be used
    var_listToDo = []
    var_stringToDo = ""
    var_intTodo = 0
    var_boolWhileCycle = True

    while var_boolWhileCycle:
        var_userSelection = input("Operation to be made: \n"
                                  "1. Add Item...       (Add / '1') \n"
                                  "2. Show Item...      (Show / '2') \n"
                                  "3. Edit Item...      (Edit / '3') \n"
                                  "5. Exit program...   (Exit / '5') \n")
        var_userSelection = var_userSelection.strip()
        var_userSelection if var_userSelection.isdigit() else funct_userOptionString(var_userSelection)
        match int(var_userSelection):
            case enum_userOptions.Add.value:
                print("Add item to the list... \n")
                # Obtain info from user
                var_stringToDo = input()
                # Add String to the list
                var_listToDo.append(var_stringToDo)
            case enum_userOptions.Show.value:
                funct_showListItems(var_listToDo)
            case enum_userOptions.Edit.value:
                var_intTodo = int(input("Select item to EDIT... "))
                funct_showListItems(var_listToDo)
                if var_intTodo > 0:
                    var_listToDo[var_intTodo - 1] = input(var_stringToDo)
                else:
                    var_listToDo[var_intTodo] = input(var_stringToDo)
            case enum_userOptions.Exit.value:
                # Terminate the program
                var_boolWhileCycle = False

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
