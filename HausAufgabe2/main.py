
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
            if not l_boolWordExist:
                # If the word does not exist, add it to the list and init in 1
                l_intWordCounter.append(l_varStringUpperCase, 1)
            if index[0] == l_varStringUpperCase:
                # Word already exists
                index[1] += 1
                l_boolWordExist = True
                break
    return l_intWordCounter


def count_word_appearances(input_string):
    # Split the input string into words using spaces as separators
    words = input_string.split()

    # Initialize a list to store words and their counts as [word, count]
    word_counts = []

    for word in words:
        # Convert the word to lowercase to make the comparison case-insensitive
        lowercase_word = word.lower()

        found = False
        for entry in word_counts:
            if entry[0] == lowercase_word:
                # If the word is already in the list, increment its count
                entry[1] += 1
                found = True
                break

        if not found:
            # If the word is not in the list, add it with a count of 1
            word_counts.append([lowercase_word, 1])

    return word_counts


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    l_intNumberOfWords = funct_separatorsInString("Tom eats and eats pasta eats")
    print(f"Total number of words... {l_intNumberOfWords}")