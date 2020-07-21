# Iterators
'''
1. iterater is use to perform iteration
2. for perfmoring iteration we have 2 objects __iter__() and __next__()

Meaing of iteration:

1. in this case we use list,tuple,set and dict
'''

for num in range(10):
    print(num)

# using iter and next
listForIter = ['ravi','ram','shyam']
print('List for iter values: ',listForIter)
# first need to use iter methods to get the values 
myit = iter(listForIter)

print('\n\nnext value: ',next(myit))
print('\n\nnext value: ',next(myit))
print('\n\nnext value: ',next(myit))
# print('\n\nnext value: ',next(myit))

# normal class
class MyClass:
    # def __init__(self, number):
    #     self.n = number

    # def outpute(self):
    #     print('\nTHis is number: ',self.n)

    # first creat iter
    def __iter__(self):
        self.n = 1
        # for passing self value to next must resturn
        return self

    def __next__(self):
        # condtion to stop next at one point
        if self.n < 10:
            # fist to recive n value from iter       
            n = self.n
            # now must to incremtnt the slef.n value
            self.n += 1
            return n
        else:
            raise StopIteration

# finally cret object of class
myiterClassObj = MyClass() 
myiterval = iter(myiterClassObj)    
# print('My iter value: ',next(myiterval))

for newnum in myiterval:
    print('\nNewnum values: ',newnum)


# myobj = MyClass(10)
# myobj.outpute()