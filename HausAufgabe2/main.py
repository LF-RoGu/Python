
def funct_separatorsInString(varString):
    # Modify commas for spaces
    l_stringChangeCharacters = varString.replace(',',' ')
    # Modify points for spaces
    l_stringChangeCharacters = l_stringChangeCharacters.replace('.', ' ')
    #Count the amount of spaces there is in the string
    l_stringNewString = l_stringChangeCharacters.split()
    
    return len(l_stringNewString)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    l_intNumberOfWords = funct_separatorsInString("Tom eats and eats pasta")
    print(f"Total number of words... {l_intNumberOfWords}")