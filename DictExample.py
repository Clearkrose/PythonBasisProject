d = {'Mechael':95, 'Bob':75, 'Tracy': 85}
print(d['Mechael'])

d['Adam'] = 65
print(d['Adam'])

print("Thomas" in d)

print(d.get('Thomas'))
print(d.get('Thomas', -1))
print(d)

d.pop('Bob')
print(d)

# Dict是用空间来换取时间的一种方法
# Dict的key必须是不可变对象
# 通过key计算位置的算法称为哈希算法（Hash）


# set和dict类似，也是一组key的集合，但不存储value
# 由于key不能重复，所以，在set中，没有重复的key

s = set([1, 2, 3])
print(s)

s = set([1, 2, 3, 1, 2, 5])
print(s)

s.add(5)
s.add(4)
print(s)

s.remove(1)
print(s)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

# 再议不可变对象

a = ['c','b', 'a']
a.sort()
print(a)

a = "abc"
print(a.replace('a', 'A'))
print(a)

# 对于不可变对象来说，代用对象自身的任意方法，也不会改变该对象自身的内容
# 相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的