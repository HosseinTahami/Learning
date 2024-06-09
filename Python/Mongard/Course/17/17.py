# Without Context Manager
file = open('text.txt', 'r')
print(file.read())
file.close()
print(file.closed)

# With Context Manager
with open('text.txt', 'r') as file:
    print(file.readlines())
print(file.closed)

with open('text.txt', 'r') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
print(file.closed)

with open('text.txt', 'r') as file:
    print(file.read(27))
    print(file.tell())
    print(file.read(13))
    print(file.tell())
print(file.closed)

with open('text.txt', 'r') as file:
    print(file.seek(27))
    print(file.read(13))
print(file.closed)

with open('text2.txt', 'w') as file:
    file.write("Hello World!\n")
print(file.closed)

with open('text2.txt', 'a') as file:
    file.write("My name is Hossein!\n")
print(file.closed)
