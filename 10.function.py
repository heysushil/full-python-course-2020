# what is function
# type of function:
# 1. pre-defined
# 2. user-define

# creating function: def

# function define
# in funcition box pass a arguments
# in function body at last we retrun a messagar or final output
def userfun():
    print('Hello function')

# call fucntion
userfun()

# way of using function

# function without arg and return Value
def user1():
    print('Hello new without arg and return fun')

user1()

# function with arg and return value 
def user2(course):
    return 'Message recived {}'.format(course)
    # print('hello')

# calling function
print(user2('Mr. Python'))

# function with arg without retrun
def funWithoutRerutn(name):
    print('Hello ',name)

name = input('Enter your name: ')
funWithoutRerutn(name)
# function without arg with return
def funWithRetrun():
    return False

# print(funWithRetrun())
if funWithRetrun() == True:
    print('Thank you funWithRetrun()')
else:
    print('Sorray funWithRetrun()')  

# how to pass multiple arg at once using * (tuple)
print('\n\n\n')
def allusers(*n):
    # print('type of n:', type(n))
    for x in n:
        print('Hello ',x)

allusers('Ram','Shyam','Geeta','Seeta')

# passing arg with keys
def details(**data):
    print('\nDetails name: ',data['name'],' ',data['email'])

details(name='Hari',course='python',email='hari@g.com')

# how to pass keword arg at once using ** (dict)

# default parameter value as arg
def argumentFun(name='Defaul'):
    print('Hello ',name)

argumentFun()   


def sum(num1, num2):
    add = num1 + num2
    print('Your sum value is ',add)

# funcaiton call
# concatnation is working with string values and in case of normal input it will always give stirn value
num1 = int(input('Enter first numebr: '))
num2 = int(input('Enter second number: '))
sum(num1, num2)

'''
Programss:

1. creat function in with print welcome message.

2. crete fucntion in whcich revie 2 user name and show them with welcome message.

3. create a funciton in which recive more then 3 friends and retrung them with thank message and show the output.

4. creat a function to perform sum,subtract, mul, div individauly.
'''