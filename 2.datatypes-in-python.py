'''
Discussion topiscs:

What is predefined keywords.
Behaviour of predefined keywords.
How many predefined keywords in python.

Example keyword:

if, else, for, while, try, except, in, is

Function / Method
1. pre-defined / 2. user-define

print()
'''

# Topics of DataTypes
'''
Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

1. Text Type:	str
2. Numeric Types:	int, float, complex
3. Sequence Types:	list, tuple, range
4. Mapping Type:	dict
5. Set Types:	set, frozenset
6. Boolean Type:	bool
7. Binary Types:	bytes, bytearray, memoryview

Extra:

1. c / c++ / php etc me char keyword milta hai
'''

# code area
name = 'Mr. Python'
print(type(name))
print('Name: ',name)

# int value wo normal number hote hain. Matlab possitive and negative
intnum = 878787 # accept possitive & negatives numbers
print('\n\nIntnum: ',type(intnum))
floatnum = 878768.987987 # float = decimal number ye bhi +/-
print('FLoatnum: ',type(floatnum))
# complex number: use j after int or float +/-
complexnum = 9898j
print('complexnum: ',type(complexnum))

# sequence datatypes

# list: [] - big bracket
# index array => array(1,2,3,4,5);
listval = [1,2,3,4,5,'hello']
print('Listval: ',type(listval))

# tuple: ()
# tupleval = (1,2,3,4,5,'hello')
tupleval = ('Hello',)
print('Tupleval: ',type(tupleval))

# range
rangval = range(6)
print('Rangval: ',type(rangval))


# dict = dictonary => key and value ki mapping {}
# associative array => array('name'=>'shubham')
dictval = {'name':'Python'}
print('Dictval: ',type(dictval))

# set: union / intersection => {}
setval = {1,23,4,5}
print('Setval: ',type(setval))

# boolean = binary => yes/no or 0/1
booleanval = bool(767)
print('Boolval: ',type(booleanval))

'''
Qestiong:

1. python data-types ye kitne bit ya byte store lete hain.
2. index array kya hota hai?
3. diffrence b/w list and tuple
4. what is associative array
5. what is set in python
6. diff b/w dict and set
'''