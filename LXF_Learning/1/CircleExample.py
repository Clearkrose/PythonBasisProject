names = ["Jack", "Nike", "Nancy"]
for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8 ,9 ,10]:
    sum = sum + x
print(sum)

# 计算从1-n的整数之和
# print(list(range(5)))
sum = 0
a = list(range(101))
for n in a:
    sum += n
print(sum)

sum = 0
n = 99
while n > 0:
    sum += n
    n = n - 2
print(sum)

# break
n = 1
while n < 100:
    if n > 10:
        break
    print(n)
    n += 1
print("END")

# continue
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    print(n)