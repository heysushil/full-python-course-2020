# class: varibale + method : object

# hamesa class neame wo capital letter 

class Myclass:
    name = 'Python'

# create class object
obj = Myclass()

print(obj.name)

# creat a cons. in class
class User:
    # createing construcre: it helps to pass values to each methods
    # self: it's a current instance which holds current value and byt htee helpf of self we will pass values to any emthod
    def __init__(self, name, course):
        self.name = name
        self.c = course
        self.address = 'India'

    def userDetails(self):
        print('hello userdtails your name is: ',self.name,' your course name is: ',self.c,' your address is: ',self.address)

# only create obje of class
userobj = User('Mr. Ram','Python')
userobj.userDetails()

# other object
newuser = User('Ravi','PHP')
# del newuser.name
newuser.userDetails()
# print(userobj.name)

class NewUserREgistration:
    pass


# new class
class HelloUser:
    def __init__(self, users):
        self.u = users
    
    def users(self):
        print('Hell all users: ',self.u)

# obj of HelloUser
# userslist = ['Ravi','Hemma','Pushpa','Neelam']
username = input('Enter your name: ')
user = HelloUser(username)        
user.users()



# proper class
class UserDetilas:
    def __init__(self, name, course, addr):
        self.n = name
        self.c = course
        self.a = addr

    # method to show user detials
    def showUserDetails(self):
        print('''
        Hello {}, how are you.
        Your course is {},
        and your finall address is {}
        '''.format(self.n,self.c,self.a))

    def welcomeMessage(self):
        # chekc conditon
        if self.n == 'Ayman' or self.n == 'ayman':
            print('Welcome ',self.n)
        else:
            print('Welcome new user ',self.n)

# create obj of UserDetilas
name = input('Enter your name: ')
course = input('Enter your course name: ')
addr = input('Enter your address: ')
mydetails = UserDetilas(name, course, addr)
mydetails.showUserDetails()
# mydetails.welcomeMessage()

'''
Programs:

1. create class in which you have 2 mthods and first one use to get the user details like name, mobile, email etc and on oher method you will show the detials. Remmber input work done into first method and you will pass it to another mthod.

2. creat a class in which you will recive dict data and which you show using multip line sting in method and also your dict data is someting like : studetn anem, father name, mother name, class. on mehtod also check if class is 2nd then show wlecome2nd class message with studetn name or if class is 3rd then show the same fo 3rd or 4th or 5th.
'''