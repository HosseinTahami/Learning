# append
names = ['Hossein', 'Kevin', 'Bob', 'Admin',
         'Ali', 'Tahami', 'Hossein', 'David']
names.append('Richard')
print(names)

# extend
names = ['Hossein', 'Kevin', 'Bob', 'Admin',
         'Ali', 'Tahami', 'Hossein', 'David']
names.extend(['Ali', 'Hossein', 'Gabriel'])
print(names)

# insert
names = ['Hossein', 'Kevin', 'Bob', 'Admin',
         'Ali', 'Tahami', 'Hossein', 'David']
names.insert(2, 'Rex')
print(names)

# remove
names = ['Hossein', 'Kevin', 'Bob', 'Admin',
         'Ali', 'Tahami', 'Hossein', 'David']
names.remove('Hossein')
print(names)

# pop
names = ['Hossein', 'Kevin', 'Bob', 'Admin',
         'Ali', 'Tahami', 'Hossein', 'David']
print(names.pop(3))
print(names)

# clear
names = ['Hossein', 'Kevin', 'Bob', 'Admin',
         'Ali', 'Tahami', 'Hossein', 'David']
names.clear()
print(names)

# index
names = ['Hossein', 'Kevin', 'Bob', 'Admin',
         'Ali', 'Tahami', 'Hossein', 'David']
print(names.index("Hossein"))
print(names.index("Hossein", 4, 7))

# count
names = ['Hossein', 'Kevin', 'Bob', 'Admin',
         'Ali', 'Tahami', 'Hossein', 'David']
print(names.count("Hossein"))

# sort
names = ['Hossein', 'Kevin', 'Bob', 'Admin',
         'Ali', 'Tahami', 'Hossein', 'David']
names.sort()
print(names)

# reverse
names = ['Hossein', 'Kevin', 'Bob', 'Admin',
         'Ali', 'Tahami', 'Hossein', 'David']
names.reverse()
print(names)

# del
names = ['Hossein', 'Kevin', 'Bob', 'Admin',
         'Ali', 'Tahami', 'Hossein', 'David']
del names[1:4]
print(names)
