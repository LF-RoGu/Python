
unsortedList = \
[
    {'event': 'Kosmos: Eine unendliche Reise', 'place': 'Phoenix des Lumières', 'date': '01.01.2024', 'price': 15},
    {'event': 'Winterleuchten', 'place': 'Westfalenpark Dortmund', 'date': '01.01.2024', 'price': 0},
    {'event': 'Konflikte', 'place': 'DASA Arbeitswelt Ausstellung', 'date': '01.01.2024', 'price': 0},
    {'event': 'Bio.Inspiration', 'place': 'DASA Arbeitswelt Ausstellung', 'date': '01.01.2024', 'price': 0},
    {'event': 'Kosmos: Eine unendliche Reise', 'place': 'Phoenix des Lumières', 'date': '02.01.2024', 'price': 15},
    {'event': 'REMIX. 800 Jahre Kunst entdecken', 'place': 'Museum für Kunst und Kulturgeschichte', 'date': '02.01.2024', 'price': 0},
    {'event': 'Emerging Artists', 'place': 'UZWEI im Dortmunder U', 'date': '02.01.2024', 'price': 0},
    {'event': 'Winterleuchtenwerkstatt', 'place': 'Regenbogenhaus im Westfalenpark', 'date': '02.01.2024', 'price': 0},
    {'event': 'Staying West', 'place': 'schauraum: comic + cartoon', 'date': '02.01.2024', 'price': 0},
    {'event': 'Kunst -> Leben -> Kunst', 'place': 'Museum Ostwall im Dortmunder U', 'date': '02.01.2024', 'price': 0}
]
# Example of lambda being used, where
# unsortedList -> item list to be sorted
# key=lambda -> A function that is applied to each element of the iterable, and the result of this function determines the sorting order. If not provided, the default behavior is to sort elements in their natural order.
# x: x[''] -> rule to sorte with
sortedList = sorted(unsortedList, key=lambda x: x['event'])

for index in sortedList:
    print(index)
