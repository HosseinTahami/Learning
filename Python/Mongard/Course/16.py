ages = {
    'Hossein': 12,
    'David': 23,
    'Kevin': 45,
    'Richard': 76,
    'John': 100,
    'Dina': 33,
    'Tahami': 56,
}

for name, age in ages.items():
    print('{} is {} years old !'.format(name, age))

for name, age in ages.items():
    print('{0} is {1} years old !'.format(name, age))

for name, age in ages.items():
    print('{1} is {0} years old !'.format(age, name))

for name, age in ages.items():
    print('{n} is {a} years old !'.format(n=name, a=age))
