# inheritance

'''
fucntion
class: fucntion => mehtod
    Inheritance
        Parent
        child
'''

# parent class
class MondayClass:
    def __init__(self, name1, name2):
        self.n1 = name1
        self.n2 = name2

    def mondayClassOutput(self):
        print('Hi, ',self.n1,' and ',self.n2)

# class obj
# myobj = MondayClass('Ayman','Megha')
# myobj.mondayClassOutput()

# child class
class TusedayClass(MondayClass):
    # override
    def __init__(self, name1, name2, message):
        # remeber parent class have 2 arguments and in case of child casls it's only recive 2 arguments for parent class.
        # thats why these 2 arguemtns must pass to parent class vie child class
        # MondayClass.__init__(self, name1, name2)

        # short cut or use super() method to pass arguemtns to parent class constructer
        super().__init__(name1, name2)
        self.m = message

    def chilMethodOutput(self):
        print('\n',self.m)
        print('\nHi i am child class method.')
        

# create child obj
# on TuesdayClass get 2 args which will pass to prent class
# message = input('Enter your message: ')

# childObj = TusedayClass('Ravi','Raj',message)
# childObj.mondayClassOutput()
# # class child calss method
# childObj.chilMethodOutput()

# anohter class
'''
a = parent class
b(a) = child class
c(b) = child class
d(c) = child class
'''

class SubChildClass(TusedayClass):
    pass

# crea obj
subChildObj = SubChildClass('Neha','Suman','Hi class')
subChildObj.chilMethodOutput()
# access mondayclass method
subChildObj.mondayClassOutput()


# multilevel inheritance
class MainClass:
    def __init__(self, name):
        self.n = name

    def name(self):
        print('\n\nMy name: ',self.n)

# another super class
class OhterMainClass:
    def __init__(self, course):
        self.c = course
    
    def course(self):
        print('My couser: ',self.c)

# child class which use 2 parent classes
class ChildClass(MainClass, OhterMainClass):
    def __init__(self, name, course):
        MainClass.__init__(self, name)
        OhterMainClass.__init__(self, course)

# obj 
mychildOBj = ChildClass('Neha', 'Python')
mychildOBj.name()
mychildOBj.course()

'''
Program:

1. creat class of calculater in which you will define individual methods for sum, subtract, multiplication. div and inherit parent class on child class name: Student, in studetn class you will define method to get studet infromation like name, school, class and show the detils then on other methods which is studetnMarks in which you will get studetn subjects mark like hindi, englis, schi etc and using parent class calulate them and also in parent class have method for find percentage of students mark. then also have other child class named Result in which you will show the studetn resutl by muliline stirng on result format as output.
'''