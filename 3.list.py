# मेरे Youtube चैनल को सबस्क्राइब करना ना भूलो ताकि आपको कोड का पूरा फ़्लो समझमे आए - https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg

# कोई भी सवाल है उसको मेरे यूट्यूब चैनल के कमेन्ट या डिस्कशन सेक्शन मे पूछ सकते हो - https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg/discussion

# और हाँ GitHub पर मुझे फॉलो करना ना भूलो ताकि सारे अपडेट एण्ड वर्क आपको मिलता रहे। 

'''
List: []

list values ko index ke form rakhta hai
list me values ko: new value add/ dellet / remove/ change
list me hum single value, list , tuple, set, dict
'''

# list
newlist = [11,12,13,14,15,16]

# check data type by type()
print('\n\nWelcome to list')
print('Datatype of newlist: ',type(newlist))

# fetch index value: list index value always start from 0
print(newlist)
print('newlist[0]: ',newlist[3])
# newlist[startpoint:endpoint]
print('define start point: ',newlist[3:])
print('define end point: ',newlist[:3]) # n-1
print('start and end point: ',newlist[1:3])

# same start and end poitn using negative value

print('negative number newlist[-1]: ',newlist[-1])
print('negative stant and end point: ',newlist[-4:-1])

# update new value on list index possition
newlist[0] = 111
newlist.insert(1,122)

# find lenght of list
print('Check list length: ',len(newlist))

# add new number in list
newlist.append(17)

# remove list value
newlist.remove(17)

# reove list value by index posstion
newlist.pop(5)

# delete list or value
del newlist[0]

# clear
# newlist.clear()

# copy list
nextlist = newlist.copy()

# join
thirdlist = newlist + nextlist
newlist.extend(thirdlist)

# list()
oldlist = [newlist,nextlist,thirdlist]


print('\nNewlist: ',newlist)
print('Nextlist: ',nextlist)
print('Thiredlist: ',thirdlist)
print('\n\nOldlist: ',oldlist)
print(oldlist[2][2])
'''
Questions: 

1. index array
2. associative array
3. diff b/w list and tuple
4. diff b/w remove/pop/del/clear
'''


'''
Program:

1. list ke sabhi method ka example bana hai aur comment likh se samjhana hai.
'''