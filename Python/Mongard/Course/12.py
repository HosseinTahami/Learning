""" Remove the repeated items !
    sets are unordered !
"""
names = {'Amir', 'Hossein', 'Jack', 'David', 'Hossein'}
print(names)

letters = set("Hossein Tahami")
print(letters)

a = set("abracadabra")
b = set("alacazam")

print(1, a - b)  # letters in a but not in b
print(2, a | b)  # letters in a or b or both
print(3, a & b)  # letters in both a and b
print(4, a ^ b)  # letters in a or b but not both
