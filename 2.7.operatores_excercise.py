# 1. Arithmatic Op (Math ke sare signs):
a = 5
b = 15
print('\nAdd: ', a + b)

print('\nSUb: ', a - b)

print('\nMul: ', a * b)

print('\nDiv: ', b / a)

print('\nModules: ', a % b)

print('\nFloor: ', 50 // 5)

print('\nExponent: ', 10 ** 2)


# 2. Assigment Op (=):
a = 10
b = 20

# b = b + a
b += 5
print('\nB: ', b)


# 3. Comparison Op (< > ! ==):
a = 10
b = 20
print('\nEqual to: ', a == b)
print('\nNot equal to: ', a != b)
print('\nGreater then: ', a > b)
print('\nGreate then equal to: ', a >= b)
print('\nLess then: ', a < b)
print('\nLess then equlal to: ', a <= b)


# 4. Logical Op (and or not):
a = 10
b = 20

print('\nand: ', a < b and b < a)
print('\nor: ', a < b or b < a)
print('\nnot: ', not a)

# 5. Identity Op (is, is not):
print('\nChek a and b: ', a is b)
print('\nChek is not: ', a is not b)


# 6. Membership Op (in, not in):
mylist = [1,2,3,4]
print('\nChekc list: ', 3 in mylist)
print('\nUse not in: ', 4 not in mylist)

# 7. Bitwise Op (True/False):
a = 10
b = 20

print('\nBitwise &: ', a & b)