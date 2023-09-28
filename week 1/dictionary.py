# dictionary is a collection of key value pairs. key is unique and value can be duplicate
person = {
    'name': 'john',
    'age': 25,
    'city': 'new york'
}
print(person)
print(person['name'])
print(person.keys())
print(person.values())

person['address'] = 'chicago'
print(person)

#dictionary is mutable/ changeable unlike tuples
person['name'] = 'jane'
print(person)

del person['address']
print(person)

for item in person:
    print(item)

for key,value in person.items():
    print(key,value)