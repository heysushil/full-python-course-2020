# Scope: local and global
# gloabl variable
num = 50
# function
def myfunction():
    # change the scope of num
    global num
    num = 10
    print('\nNum: ',num)
    # creat inner function
    # def otherFunction():
    #     print('Otherfucntion value: ',num)
    # # call inner fucntion in side main fucntion
    # otherFunction()

myfunction()

# using fucniton num out side the funciton
print('\nNum: ',num)

# python gloable keyword 
