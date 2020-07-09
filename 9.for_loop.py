# मेरे Youtube चैनल को सबस्क्राइब करना ना भूलो ताकि आपको कोड का पूरा फ़्लो समझमे आए - https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg

# कोई भी सवाल है उसको मेरे यूट्यूब चैनल के कमेन्ट या डिस्कशन सेक्शन मे पूछ सकते हो - https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg/discussion

# और हाँ GitHub पर मुझे फॉलो करना ना भूलो ताकि सारे अपडेट एण्ड वर्क आपको मिलता रहे। 

# for loop

'''
while loop

intilaize
while(condtion):
    while body
    incre/ decre
'''

students = ['ram','shyam','seeta','geeta']

# s is varaible which stores values of list one by one
for s in students:
    print('Hello ',s,' welcome in python class.')

# stirng
name = 'megha'
print('\nName: ',name[0])
for n in name:
    print(n)

# dict
print('\n\nDict output')
students = {'name':'megha','email':'megha@g.com'}
for s in students:
    print(s,' : ',students[s])

# range
print('\n\nRang \n')
# in range if we give only one number it will start form 0 and end at n-1 posstion
# range(start,end,diff)
for r in range(0):
    print(r)
else:
    print('\n2s table ended.')

'''
while
for
do while
'''

# nested loop
name = ['megha','ayman','ram','shyam']
course = ['python','timing 10 - 11']

print('\n\nNested loop\n')
for n in name:
    print('Hello ',n,'\n')

    # create loop in n loop
    print('''
        --------------------
        Your Detsils is
        --------------------\n
        ''')
    for c in course:
        print(c)
    print('\n')

