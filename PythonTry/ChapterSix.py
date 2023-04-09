print(r'That is Carol\'s cat.')

print('''a
        v
    d
    
    bdddfdasj;lfk
    end''')

'''
多
行
注
释
'''

'''
    .isupper()
    .islower()
    .isalpha() 返回True，如果字符串只包含字母，并且非空
    .isalnum() 返回True，如果字符串只包含字母和数字，并且非空
    .isdecimal() 返回true，如果字符串只包含数字字符，并且非空
    .isspace() 返回true，如果字符串只包含空格、制表符和换行，并且非空
    .istitle() 返回true，如果字符串仅包含以大写字母开头、后面都是小写字母的单词
'''

print('hello world'.startswith('hello'))
print('hello world'.endswith('World'))
print('hello world'.endswith('World'.lower()))

a = ', '.join(['abc', 'bcd', 'cde'])
print(a)

print('a,b,c,d,e,f,g'.split(','))

print('|' + 'Hello'.rjust(10, '*') + '|')
print('|' + 'Hello'.ljust(10) + '|')
print('|' + 'Hello'.center(20, '=') + '|')

spam = '  Hello world  '
print('|' + spam.strip() + '|')
print('|' + spam.lstrip() + '|')
print('|' + spam.rstrip() + '|')

# pyperclip模块有copy()和paste()函数，可以向计算机的剪切板发送文本，或从它接收文本