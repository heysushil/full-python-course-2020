# lambda
'''
Syntax of lambda function:

normal function syntax:

def functionname():
    expression

lambda arguments : expression
'''

lamdbaValue = lambda num,num1,num2 : num + num1 + num2
print('\nlambdavaleu ans: ',lamdbaValue(10,20,30))

# creating noral function with inner lambda functon
def sumNum(a, b):
    # add = a + b
    # print('\nsumNum: ',add)

    # in this step you have a and b values but lamval is a lambda function which needs to call and passs one agrument which is lam.
    # for that in our case we will return the lamval lambda fucntion, so need to pass lam argument from outside the sumNum function
    lamval = lambda lam : lam + a + b
    return lamval
    # print('lamval(): ',lamval(100))

# call sumnum funciton
# forPassingLamVal is a varibale which holds the lambda function and in this case neet to be pass lam argument value
forPassingLamVal = sumNum(10,20)
lam1 = sumNum(50,100)

print('\n\nforPassingLamVal: ',forPassingLamVal(200))
print('\n\nlam1: ',lam1(500))

'''
Programss

1. creat a function in whcih recive 4 different numbers and also check if user insert otherthen integer value then show not accepted input message to user otherwise in function use lambda fucntion to give one admin number and then perform addition, multiplication, div and subtraction functions seprately with same concepts.
'''