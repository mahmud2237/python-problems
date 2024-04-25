Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'2' + '4'
'24'
x = 'Hello World'
x
'Hello World'
print(x)
Hello World
x.upper()
'HELLO WORLD'
print(x.lower())
hello world
x = "I love You"
print(x.upper().split('oveu'))
['I LOVE YOU']
print(x.upper.split('oveu'))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(x.upper.split('oveu'))
AttributeError: 'builtin_function_or_method' object has no attribute 'split'
print(x.split('oveu'))
['I love You']
print(x.split('ou'))
['I love Y', '']
print(x.split('ove', 'ou'))
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(x.split('ove', 'ou'))
TypeError: 'str' object cannot be interpreted as an integer
print('This is a string []' + .format('INSERTED'))
SyntaxError: invalid syntax
print('This is a string {}' + .format('INSERTED'))
SyntaxError: invalid syntax
print('This is a string {}'.format('INSERTED'))
This is a string INSERTED
a = 'am'
b = 'a'
c = 'Engineer'
print('I {} {} {}'.format(a, b, c))
I am a Engineer
print('I {0} {2} {2}'.format(a, b, c))
I am Engineer Engineer
print(f'I {a} {b} {c}')
I am a Engineer



print('Now jump to the LISTs')
Now jump to the LISTs
>>> my_list = [1, 2, 3]
>>> print(my_list)
[1, 2, 3]
>>> 
>>> my_list = ['String', 100, 23.4]
>>> print(my_list)
['String', 100, 23.4]
>>> len(my_list)
3
>>> another_list = [4, 5, 6]
>>> new_list = my_list + another_list
>>> print(new_list)
['String', 100, 23.4, 4, 5, 6]
>>> type(new_list)
<class 'list'>
>>> new_list.append("six")
>>> new_list
['String', 100, 23.4, 4, 5, 6, 'six']
>>> new_list.remove(new_list[6])
>>> new_list
['String', 100, 23.4, 4, 5, 6]
>>> new_list.reverse()
>>> new_list
[6, 5, 4, 23.4, 100, 'String']
>>> new_list.pop('seven')
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    new_list.pop('seven')
TypeError: 'str' object cannot be interpreted as an integer
>>> new_list.pop()
'String'
>>> new_list.append('six', 7)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    new_list.append('six', 7)
TypeError: list.append() takes exactly one argument (2 given)
>>> new_list.append('six')
>>> new_list
[6, 5, 4, 23.4, 100, 'six']
>>> 
>>> 
>>> 
>>> print('Now we will workig with Dictonary')
Now we will workig with Dictonary
>>> my_dict = {'key1': 'value1', 'key2': 'value2'}
>>> my_dict
{'key1': 'value1', 'key2': 'value2'}
>>> my_dict['key1']
'value1'
>>> 
>>> prices_lookup = {'apple': '2.99', 'oranges': '4.49', 'milk': '5.00'}
>>> prices_lookup['milk']
'5.00'
>>> prices_lookup = {'apple': 2.99, 'oranges': 4.49, 'milk': 5.00}
>>> prices_lookup['oranges']
4.49
>>> 
>>> d = {'key1': ['a', 'b', 'c']}
>>> d['key1'][2].upper()
'C'
d = {'k1': 100, 'k2': 200}
d
{'k1': 100, 'k2': 200}
d['k3'] = 300
d
{'k1': 100, 'k2': 200, 'k3': 300}
d['k1'] = 'NEW VALUE'
d
{'k1': 'NEW VALUE', 'k2': 200, 'k3': 300}

print("Let's see all key values in d")
Let's see all key values in d
d.keys()
dict_keys(['k1', 'k2', 'k3'])
d.values()
dict_values(['NEW VALUE', 200, 300])
d.items()
dict_items([('k1', 'NEW VALUE'), ('k2', 200), ('k3', 300)])
