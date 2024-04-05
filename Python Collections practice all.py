Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
myList = ["red", "blue", "green"]
myTuple = ("red", "blue", "green")
myList.append("white")
print(myList)
['red', 'blue', 'green', 'white']
myTuple.append("white")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    myTuple.append("white")
AttributeError: 'tuple' object has no attribute 'append'
print(dir(myList))
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
print(dir(myTuple))
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

mySet = {"red","blue", "green"}
print(type(mySet))
<class 'set'>
print(dir(mySet))
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
print(mySet[1])
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(mySet[1])
TypeError: 'set' object is not subscriptable









mySet.add("purple")
print(mySet)
{'blue', 'red', 'purple', 'green'}
print(mySet.reverse)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(mySet.reverse)
AttributeError: 'set' object has no attribute 'reverse'
>>> print(myList.reverse)
<built-in method reverse of list object at 0x000002449EA68140>
>>> print(myTuple.reverse)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(myTuple.reverse)
AttributeError: 'tuple' object has no attribute 'reverse'
>>> print(myList)
['red', 'blue', 'green', 'white']
>>> 
>>> print(len(myList))
4
>>> print(len(myTuple))
3
>>> print(len(mySet))
4
>>> mySet.remove('green')
>>> print(mySet)
{'blue', 'red', 'purple'}
>>> 
>>> 
>>> #working with set
>>> A = {1, 3, 5, 8}
>>> B = {2, 4, 6, 7}
>>> A.union(B)
{1, 2, 3, 4, 5, 6, 7, 8}
>>> B.union(A)
{1, 2, 3, 4, 5, 6, 7, 8}
>>> B.add(9)
>>> print(B)
{2, 4, 6, 7, 9}
>>> A.intersection(B)
set()
>>> A.difference(B)
{8, 1, 3, 5}
>>> B.difference(A)
{2, 4, 6, 7, 9}
>>> 
>>> # working with Dictionary
>>> newDic = {100:"Patrick", 200:"joe", 300:"martin"}
>>> print(newDic)
{100: 'Patrick', 200: 'joe', 300: 'martin'}
>>> newDic[200]
'joe'
>>> newDic[400]= "priti"
>>> print(newDic)
{100: 'Patrick', 200: 'joe', 300: 'martin', 400: 'priti'}
