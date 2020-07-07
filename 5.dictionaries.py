# Ditionaries
#{key:value}
user = {'name':'Hari','course':'python'}

print('newd: ',type(user))
print('user: ',user['name'])

# add
user['mobile'] = 989879879
print('user: ',user)

# change
user['mobile'] = 999999999
print('updated user: ',user)

# pop
user.pop('course')
print('pop user course: ',user)

user['dob'] ='09th july'
print('user: ',user)
# popitem
user.popitem()
print('updted user: ',user)

# del
del user
# print(user)

# multilevel dictionary
detail = {
    'Hari': {
        'email':'hari@gamil.com',
        'mobile':987987987
    },
    'Shyam': {
        'email':'shyam@gmai.com',
        'mobile':87987987,
        'Eductaion': {
            'BCA': '98%',
            'MBA': '76%'
        }
    }
}
print('\ndetails: ',detail)
print('hari details: ',detail['Shyam']['Eductaion']['BCA'])

# copy
newdetial = detail.copy()
print('\nnewdetial: ',newdetial)

# clear
detail.clear()
print('details: ',detail)

# keys
print('\nnewdetial.keys(): ',newdetial.keys())

# values()
print('\nnewdetial.values(): ',newdetial.values())


'''
Homework:

update()
formkeys()
get()
items()
'''

'''
Programs:


'''

