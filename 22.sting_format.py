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