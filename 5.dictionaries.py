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

Normal Questions:

1. Diye gaye dict me brad ki salary update karke 8500 karni hai:
sampleDict = {
     'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}
}

Expected output:
sampleDict = {
     'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 8500}
}

2. Ye do list hai inko dictionary me convert karna hai:
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
Output kuch aysa hona chaiye: 

{'Ten': 10, 'Twenty': 20, 'Thirty': 30}
In 2 dictionary ko ek sath marg karo:
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
Aur iska output kuch aysa mulna cahiye:
{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}


3. Is diye gaye dict mese history ki value ko show karao:
sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
Expected answer: 80


4. Diyegaye list ko as a key aur diyegaye dict ko as a value set karo:
employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}
Dict me check karna hai ki kya 200 value exist karta hai ya nahi:
sampleDict = {'a': 100, 'b': 200, 'c': 300}
Expected output:
True


5. Diye gaye dict me city ko rename karke location karna hai:
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
 
Expected output:
{
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "location": "New york"
}


6. Diye gaye dict me jis subject ka bhi marks sabse kam hai usko find kar ke show karna hai:
sampleDict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
Expected output:
Math

Advance Questions:

7. Diye gaye dict mese niche bataye keys ka use kar ke new dict banao:
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
  
}
Ye keys use karna hai:
keys = ["name", "salary"]

		Output:
		{'name': 'Kelly', 'salary': 8000}

8. Dict mese following keys ko remove karna hai:
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
  
}
keysToRemove = ["name", "salary"]
Expected output:
{'city': 'New york', 'age': 25}

'''

