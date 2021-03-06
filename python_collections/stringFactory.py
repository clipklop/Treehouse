# Create a function named string_factory that accepts a list of dictionaries and a string.
# Return a new list build by using .format() on the string, filled in by each of the dictionaries in the list.

dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasanga'},
    {'name': 'Walter',
     'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
]

string = "Hi, I'm {name} and I love to eat {food}! \r"

def string_factory(dicts, string):
	strings = []
	for key in dicts:
		strings.append(string.format(**key))
	return strings

print(string_factory(dicts, string))
