
def funct_separatorsInString(varString):
    #Count the amount of spaces there is in the string
    l_stringNewString = varString.split()

    # Init dictionary list
    l_intWordCounter = []

    for varStringUpperCase in l_stringNewString:
        # Modify string to have only upper case letters
        l_varStringUpperCase = varStringUpperCase.upper()
        l_boolWordExist = False
        for index in l_intWordCounter:
            if index[0] == l_varStringUpperCase:
                # Word already exists
                index[1] += 1
                l_boolWordExist = True
                break
        if not l_boolWordExist:
            # If the word does not exist, add it to the list and init in 1
            l_intWordCounter.append([l_varStringUpperCase, 1])
    return l_intWordCounter

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    l_intNumberOfWords = funct_separatorsInString("Tom eats and eats pasta eats")
    print(f"Total number of words... {l_intNumberOfWords}")