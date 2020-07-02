'''
Tuple

1. tuple ki values non-changeable hoti hai
2. immutable
3. tuple syntax = ()
4. tuple andar bhi values index fke form me hoti hai
'''

newtuple = ('Ram','Shyam','Geeta','Seeta')

# chekc datatype
print('\n\nnewtupels dataype: ',type(newtuple))

# tuple me agar single value hai then value ke baad ek comma use karna jaruru hi
checktupe = ('Hello',)
print(type(checktupe))

# range of tuple
print('newtuple[0]: ',newtuple[0])
print('start and end: ',newtuple[0:3])  # 3-1

# try to modify tuple value
# newtuple[0] = 'Shree Ram'

# len
print('count tupe: ',len(newtuple))

# remove ke liye del
# del newtuple


# join or concatanation +
secondtuple = ('Hari','Ravi','Sona')
addtuple = newtuple + secondtuple
print('\naddtuple: ',addtuple)

# convert tupel into list
tuple2list = list(newtuple)
print('tupel2list type: ',type(tuple2list))
tuple2list.append('Arjun')
tuple2list.append('Bheem')
tuple2list.append('Nakul')

# convert list 2 tuple
newtuple = tuple(tuple2list)
# print('list2tuple: ',list2tuple)


# tuple vlaue
print('TUple values newtupel: ',newtuple)

'''
Questions:

1. what is static variable in programming language.
2. what is constant in programming language.
3. Differnce b/w static and constant
'''

'''
programms

1. tuple me friends ke name save karne hai and unko index postion se multiline string ka use karke output show karana hai.

2. tuple negative values to output me show karke dekho

3. 1st cast ke friend list ka use karna hai aur uske andar kuch firends ko hata kar new firends ke name add karne hai. complet list ko multiline string ka use karke show karan ahi.
'''