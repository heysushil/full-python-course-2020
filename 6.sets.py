# set: index random

a = {2,3,4,5,6,7,865,3,2}
b = {4,3,2,5,6,7,6,5,5,4,38}

print('\ntype of a: ',type(a))
print('a: ',a)
print('b: ',b)

# add()
a.add(900)
# a.add()
print('a: ',a)

# update()
a.update([33,445,334,33223])
print('a update: ',a)

# len()
print('len: ',len(a))

# remove
a.remove(33223)
# a.remove(33223)
print('a: ',a)

# discard()
a.discard(445)
a.discard(445)

print('dicsard a: ',a)

# pop()
a.pop()
print('a pop: ',a)

# clear()
a.clear()
print('clear a: ',a)

# del
del a
# print('a del: ',a)

# join
print('b: ',b)

c = {3,4,5,6,8,6,4,3,4}

d = b.union(c)
print('union in d: ',d)

# update

# difference()
print('c: ',c)
print('\nb.difference(c): ',b.difference(c))

# intersection
print('b.intersection(c): ',b.intersection(c))
e = b.intersection(c)

# isdisjoint()
d = {33,444,555}
f = b.isdisjoint(d)
print('f: ',f)

# issubset()
z = b.issubset(c)
print('check issubset: ',z)

'''
Homework:

1. update() ko use karo aur chekc karo ki union and update kya similer kam karte hain?
2. difference_update() ?
3. discard() 
4. intersection_update()
5. setdefault()
'''


