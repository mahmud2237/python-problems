Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> '2' + '4'
'24'
>>> x = 'Hello World'
>>> x
'Hello World'
>>> print(x)
Hello World
>>> x.upper()
'HELLO WORLD'
>>> print(x.lower())
hello world
>>> x = "I love You"
>>> print(x.upper().split('oveu'))
['I LOVE YOU']
>>> print(x.upper.split('oveu'))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(x.upper.split('oveu'))
AttributeError: 'builtin_function_or_method' object has no attribute 'split'
>>> print(x.split('oveu'))
['I love You']
>>> print(x.split('ou'))
['I love Y', '']
>>> print(x.split('ove', 'ou'))
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(x.split('ove', 'ou'))
TypeError: 'str' object cannot be interpreted as an integer
>>> print('This is a string []' + .format('INSERTED'))
SyntaxError: invalid syntax
>>> print('This is a string {}' + .format('INSERTED'))
SyntaxError: invalid syntax
>>> print('This is a string {}'.format('INSERTED'))
This is a string INSERTED
>>> a = 'am'
>>> b = 'a'
>>> c = 'Engineer'
>>> print('I {} {} {}'.format(a, b, c))
I am a Engineer
>>> print('I {0} {2} {2}'.format(a, b, c))
I am Engineer Engineer
>>> print(f'I {a} {b} {c}')
I am a Engineer
>>> 
>>> 
>>> 
>>> print('Now jump to the LISTs')
Now jump to the LISTs
>>> my_list = [1, 2, 3]
>>> print(my_list)
[1, 2, 3]
>>> 
>>> my_list = ['String', 100, 23.4]
>>> print(my_list)
['String', 100, 23.4]
