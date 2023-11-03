string_list = ['potato', 'kartofeln', 'musli', 'bier', 'hola', 'mundo']

# Convert each word into a list of its individual letters
# The map function helps you apply a specific action to each word. In this case is to use the function 'list'
# This to create a list of lists
# map(list, strings) means -> Take each word in the list of words (strings) and turn it into a list of its letters using the list function
list_of_lists = list(map(list, string_list))

print(list_of_lists)
