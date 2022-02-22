text = 'Sample text \n\r Sample text2'
print(text)

value = '\r'

# text[4]

text = text.replace(value, '')
print(text)

# Lists

animals = ['cat', 'bat', 'rat', 'elephant']
print(animals[0])

# Dictionaries

cat = {'color': 'grey', 'name': 'Grytsyk', 6: [3, 4, 'frfr']}
dog = {'color': 'red', 'name': 'Umka'}

print(cat[6])
print(cat['name'])

print(cat.values())