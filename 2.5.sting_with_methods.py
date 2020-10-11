# single line string '' ""
# Some imp special char: , . ' " () {} [] ! / \ ; : #


name = 'Hey Sushil'
myname = "Learn Python with Hey Sushil"
print('\nName: ', name, ' Type: ', type(name))
print('\nMyname: ', myname, ' Type: ', type(myname))

# ek se jada string ko aps jodne ke liye conctanation sign (+) ka use karte hain

fullString = name + myname
print('\nfullString: ', fullString)
print('\n', name, myname)

# multiline string
mycode = '''
fullString = name + myname
print('fullString: ', fullString)
print('', name, myname)
'''
print('\nmycode: ', mycode)

mybiodata = '''
--------------------------------------------
            Hey Sushil Bio Data
--------------------------------------------
My name is Chaudhary Sushil
My YouTube channel name is Hey Sushil
--------------------------------------------
Learn Python with Hey Sushil
--------------------------------------------            
'''
print('\n', mybiodata)

# string indexing 
name = 'Hey Sushil'
print('\nname[0]: ', name[2])

'''
Indexing ke bare me aur:

1. indexing agar singl value chaiye to index postion big bracke me likho.
2. Indexing me hum start aur end point bhi decide kar sakte hain.
3. Yad rahe end point n-1 tak chalta hai.
'''
print('\nname[0:3]: ', name[0:3])
print('\nONly start point: ', name[4:])
print('\nonly end: ', name[:3])

name = 'Yad rahe end point n-1 tak chalta hai Yad rahe end point n-1 tak chalta hai Yad rahe end point n-1 tak chalta hai Yad rahe end point n-1 tak chalta hai'

# negative indexing
print('\nGet last char: ', name[-1])
print('\nGet last 3 char: ', name[-3:])

# string methods:
name = 'hey sushil'
print('\nType: ', type(name))

print('\nname.capitalize(name): ', name.capitalize())
print('\nGet index of l: ', name.index('l'))
print('\nchane hey: ', name.replace('hey', 'hello'))
print('\nsplit: ', name.split('s'))
print('\nupper: ', name.upper())