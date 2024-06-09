name = 'Hossein'
age = 24

print(name + ' is ' + str(age) + ' years old !')

# F String
print(f'{name} is {age} years old !')

ages = {
    'Hossein': 12,
    'David': 23,
    'Kevin': 45,
    'Richard': 76,
    'John': 100,
    'Dina': 33,
    'Tahami': 56,
}

print('\n')

for name, age in ages.items():
    print(f'{name} ==> {age} !')

print('\n')

for name, age in ages.items():
    print(f'{name:10} ==> {age:5} !')
