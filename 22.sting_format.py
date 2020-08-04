# sting format

name = input('Etner your name: ')
age = int(input('Enter your age: '))
email = input('Etnre your email id: ')
print('Hello, Your name is ' + name , '\nYour age is: ',age,' \nYour email id is ',email)
print('\nuseing format\n\n')

print('''
Hello use your details is

Your name is {}
Your age is {}
Your email id is {}
'''.format(name, age, email))

print('''
Hello use your details is

Your name is {0}
Your age is {1}
Your email id is {2}

Hi {0}, how are you, your age is {1} right?
'''.format(name, age, email))

print('''
Hello use your details is

Your name is {name}
Your age is {age}
Your email id is {email}
'''.format(name = name,age = age,email = email))