# using modeles function in this file
# import module as m
from module import adding2Numbers as add

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

print('\nSum result: ',add(num1, num2))

# print('\nMultiplication result: ',multiply2Numbers(num1, num2))

# print('\nUser names: ',m.listOfUsers)


# python have lot's of predienife modules
import platform as p

checkSystem = p.system()
print('\nCheck system: ',checkSystem)

print('\nCurrent platformr realted directorys: ',dir(p))


# date
import datetime as d

date = d.datetime.now()
print('\nCurrent date: ',date)
print('\nYear: ',date.year)
print('\nCurrent Day: ',date.strftime('%a'))
print('\nCurrent Day: ',date.strftime('%A'))
print('\nCurrent Month: ',date.strftime('%m'))
print('\nCurrent Year: ',date.strftime('%y'))
print('\nCurrent Year: ',date.strftime('%Y'))

print('\nComple date: {} - ({})/{} - ({})/{}'.format(date.strftime('%d'),date.strftime('%A'),date.strftime('%m'),date.strftime('%B'),date.strftime('%Y')))


# math
print('\nfind nMinimu value: ',min(4,1,2,6,3,7,9))

print('Find numerb is absolute or not: ',abs(-222.949))

print('power of 3 is 2: ',pow(3,2))

# math library
import math

print('value of pi: ',math.pi)

print('sqrt of 5: ',math.sqrt(5))
# print('other methods: ',math.)


# json: javascript object notation
import json

# json formt data
jsondata = '{"name":"ravi","course":"python"}'
print('chiech jsondata type: ',type(jsondata))

# convet jason to python dict
convetJsontoPython = json.loads(jsondata)
print('chiech jsondata type: ',type(convetJsontoPython))
print('name: ',convetJsontoPython['name'])

# python to json convertion
convetPythonToJson = json.dumps(convetJsontoPython)
print('convetPythonToJson: ',convetPythonToJson)
print('convetPythonToJson type; ',type(convetPythonToJson))

'''
Ptyhon data convet ot json
dict
list
tuple
stirng
int
float
boolean
'''
