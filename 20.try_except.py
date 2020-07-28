# try except

'''
try
except
finally
else
'''
# name = 'Python'
# print(name)
try:
    print(name)
except NameError:
    print('We dint get name yet.')    
except:
    print('Name is not get yet.')
else:
    print('finally we get else')

# finally: close() 
try:
    print(username)
except NameError:
    print('\nYou forget to give your name')
finally:
    print('Finally our work is done')


# raise keyword
name = 'Python'
if not type(name) is int:
    raise TypeError('Only integer values accept')