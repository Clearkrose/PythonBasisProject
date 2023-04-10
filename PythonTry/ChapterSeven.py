import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-333-3413')
print(mo.group())
print(mo.group(1))
print(mo.group(2))

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel.')
print(mo.group())
print(mo.group(1))

# 用问好实现可选匹配
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The adventures of Batwoman')
print(mo2.group())

# 用 * 匹配零次或多次
# 用 + 匹配一次或多次
# 用 {} 匹配特定次数   (Ha){3}    (Ha){3,} ———— 匹配3次或更多次实例    (Ha){,5}

# 贪心和非贪心匹配
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search("HaHaHaHaHaHa")
print(mo1.group())

greedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = greedyHaRegex.search("HaHaHaHaHaHa")
print(mo2.group())

# finadall()
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d\-\d\d\d\d')
mo = phoneNumRegex.findall('cell: 411-515-4623 and 341-431-4524')
print(mo)

# 插入符号（^），表明匹配必须发生在被查找文本开始处
# 美元符号（$），表明该字符串必须以这个正则表达式的模式结束
# 通配符（.），匹配除了换行之外的所有字符
# 点-星（.*），匹配任意文本，除换行外
# re.compile('.*', re.DOTALL)可以让句点字符匹配所有字符，包括换行字符
# re.compile('  ', re.I) 不区分大小写的匹配

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

# 管理复杂的正则表达式
PhoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?          # area code
    (\s|-|\.)?                  # separator
    
    )''', re.VERBOSE)

someRegxValue = re.compile('foo', re.I | re.DOTALL | re.VERBOSE)