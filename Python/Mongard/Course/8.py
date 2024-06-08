names = ['Hossein', 'Kevin', 'Bob', 'Admin', 'Ali', 'Tahami']

# Continue
for name in names:
    if name == 'Admin':
        continue
    print(name)
else:
    print("End...\n")

# Break
for name in names:
    if name == 'Admin':
        break
    print(name)
else:
    print("End...")

# Pass
while True:
    ...

while True:
    pass
