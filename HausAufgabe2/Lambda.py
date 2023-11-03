
unsortedList = \
[
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]
# Example of lambda being used, where
# unsortedList -> item list to be sorted
# key=lambda -> A function that is applied to each element of the iterable, and the result of this function determines the sorting order. If not provided, the default behavior is to sort elements in their natural order.
# x: x[''] -> rule to sorte with
sortedList = sorted(unsortedList, key=lambda x: x['color'])

for index in sortedList:
    print(index)
