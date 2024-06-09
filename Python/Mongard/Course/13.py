# Key:Value Pairs
ages = {
    'Hossein': 12,
    'David': 23,
    'Kevin': 45,
}

del ages['Hossein']

print(ages)
print('David' in ages)

print(ages.items())

for name, age in ages.items():
    print(name, 'is', age, 'years old !')

ages = dict([('Hossein', 20), ('Kevin', 22), ('John', 45)])
print(ages)
