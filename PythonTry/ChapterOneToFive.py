print("Hello", end="")
print("World")

print("Cat", "Dog", "Bee")
print("Cat", "Dog", "Bee", sep=",")

spam = ['cat', 'dog', 'bee', 'elephant']
del spam[2]
print(spam)

cat = ['fat', 'black', 'loud']
size, color, disposition = cat
print(size)

a = tuple(['cat', 'dog', 'elephant'])
b = list(('cat', 'dog', 'elephant'))
c = list('Hello')
print(a, b, c)

# 引用
spam = 42
cheese = spam
spam = 100
print(spam)
print(cheese)

spam = [0, 1, 2, 3, 4, 5]   # 指向
cheese = spam
cheese[1] = "hello!"
print(spam)
print(cheese)

# Copy
import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)
print(cheese)

picnicItems = {'apples':5, 'cop':2}
print(picnicItems.get('apples', 0))
print(picnicItems.get('egg', 0))

d = picnicItems.setdefault('color', 'black')
print(d)
print(picnicItems)

# 漂亮打印
import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
print(pprint.pformat(count))    # 等价