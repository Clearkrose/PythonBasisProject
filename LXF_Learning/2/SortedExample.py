# sorted()
print(sorted([26, 4, -12, 9, -21]))
print(sorted([26, 4, -12, 9, -21], key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))