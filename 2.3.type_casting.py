'''
Type casting kya hai?

1. Type casting ka use kiya jata hai ek data type ko dusre data type me convert karne ke liye.

Type casting kitne tarike ka hota hai?

1. Ye 2 tarike ke hote hain:
    1. implicit type conversion
    2. explicit type conversion
'''

# 1. implicit type conversion

intnum = 5000
floatnum = 5000.10

print('\nINt: ', intnum, ' type: ', type(intnum))
print('\nFloat: ', floatnum, ' Type: ', type(floatnum))

sumOfIntAndFloat = intnum + floatnum
print('\nSum: ', sumOfIntAndFloat, ' Type: ', type(sumOfIntAndFloat))


# 2. explicit type conversion

# int 2 float
int2float = float(intnum)
print('\nint2float: ', int2float, ' Type: ', type(int2float))

int2comlex = complex(intnum)
print('\nint2comlex: ', int2comlex, ' Type: ', type(int2comlex))

# float 2 int
float2int = int(floatnum)
print('\nfloat2int: ', float2int, ' Type: ', type(float2int))

float2complex = complex(floatnum)
print('\nfloat2complex: ', float2complex, ' Type: ', type(float2complex))

# complex
# complex2int = int(12j)
# print('\ncomplex2int: ', complex2int, ' Type: ', type(complex2int))

# string
name = '123'
print('\nname: ', name, ' Type: ', type(name))

name2int = int(name)
print('\nname2int: ', name2int, ' Type: ', type(name2int))



'''
Work to do after class:

1. Int, float, complex aur string ke apas me type convertion kar ke chekc karo.
2. Kya karne par shai hai aur kya karne par error aa raha hai.
3. Agar error aa raha hai to kya error aa raha hai ye dhyan dena hai.
'''