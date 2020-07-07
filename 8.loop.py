# while loop

'''
syntax of while

intilaization
while condtion:
    body
    increment or decrement
'''

a = 20
value = ['ayman','vivek','megha','hari','syam']
while a > len(value):    
    # print('Student Name: ',value[a])
    # bereak    
    # if value[a] == 'megha':
    #     # print('\nHi Ayamn')
    #     # break
    #     continue

    print('Student Name: ',value[a])    
    a += 1
else:
    print('Loop ended')
