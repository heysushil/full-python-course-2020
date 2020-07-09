# मेरे Youtube चैनल को सबस्क्राइब करना ना भूलो ताकि आपको कोड का पूरा फ़्लो समझमे आए - https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg

# कोई भी सवाल है उसको मेरे यूट्यूब चैनल के कमेन्ट या डिस्कशन सेक्शन मे पूछ सकते हो - https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg/discussion

# और हाँ GitHub पर मुझे फॉलो करना ना भूलो ताकि सारे अपडेट एण्ड वर्क आपको मिलता रहे। 

'''
Conditon:

if: for single condtion
    syntax: if (condtion):


if else: double body
    syntax: if():
                body
            else:
                body

if elif else: multiple condtions
    syntax: if():
                body
            elif(condtion):
                body
            else:
                body
'''

a = 5
b = 10

if a == b:
    print('\n Yes a == b. Sum of a and b: ',a+b)
elif(a < b):
    print('\nyes a < b.')
elif(a != b):
    print('\nYes a != b. Sum of a and b: ',a+b)
else:
    print('\nThis is else body')


# stu1 = 'ayman'
# stu2 = 'megha'
# stu3 = 'vivek'
students = ['megha','vivek','ayman','hari']

if len(students) >= 2 and students[0] == 'ayman':
    print('\nWelcome {}, Total ',len(students), 'Students present'.format(students[0]))
elif len(students) >= 1 and students[0] == 'megha' and len(students) < 3:
    print('\nWelcome Megha, Total Studnts: ',len(students))
elif not(students[3] == 'hari'):
    print('\nWe are not allow Hari in class')
else:
    print('\nNo one present')

print('\nStudnets: ',students)

# identity operator: is is not
if students[0] is 'ayman':
    print('\n Hi ',students[0], ' ',students[0] is 'megha')
elif students[0] is not 'vivek':
    print('\nOn zero posstion megha present')

# membership operators: in / not in
print('\n Chek vivke: ','mr. vivek' in students)

if 'mr. vivek' in students:
    print('\nWelcome Vivek class start now.')
elif 'ram' not in students:
    print('\nwe will wait for ram')


'''
Programs:

1. program bano jisme ki student ki list banai hai aur is list me new students ko add karna hai then agar 1 studnet hai to class wait kare gi ka message shwo karao. otherwise agar class me more then 5 students hai to class start ka message show karo. agar class me 3 studentss present hai to unke name teacher ko show karo.
'''
