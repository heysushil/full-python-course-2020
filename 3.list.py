# मेरे Youtube चैनल को सबस्क्राइब करना ना भूलो ताकि आपको कोड का पूरा फ़्लो समझमे आए - https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg

# कोई भी सवाल है उसको मेरे यूट्यूब चैनल के कमेन्ट या डिस्कशन सेक्शन मे पूछ सकते हो - https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg/discussion

# और हाँ GitHub पर मुझे फॉलो करना ना भूलो ताकि सारे अपडेट एण्ड वर्क आपको मिलता रहे। 

'''
Python Collections:

Ye 4 datatypes multiple values ko hold ya store karne ki capacity rakte hain. Is liye hi inhe collection bhi kha jata hai.
Example: Abhi tak humne int,float,comple aur set datatype use kiya but ye sabhi ek time pe ek value ko hi store kar sakte hain.
Isliye jab hame ek sath multiple values ko store karna ho single varibale me to hum yehai 4 datatypes ka use karte hain.

1. list => denote by []
2. tupe => ()
3. dict (dictonary) => {}
4. set => {}

Python List me following methods hain:

Note: Example ke liye mylist = [1,2,3,4], iske behalf par examples diye gaye hain:

1. append(): List me last se 1 nai value add karne ke liye append ka use kiya jata hai. Example: mylist.append(5)
2. clear(): clear method list ko empty karta hai. Empty karne par agar varibel ko print karoge to empty list milega. But error nahi milega. Example: mylist.clear()
3. copy(): Copy method ek list ko copy karke new variable me store kar dega. Example: newlist = mylist.copy()
4. extend(): Extend ka use karke ek se jada list ko aapsh me marge kiya jata hai. Exaple: mylist.extend(newlist)
5. index(): Index method kisi bhi value ka index position bata hai. Example: mylist.index(4)
6. insert(): Insert method list me existing index possition par new value ko update karta hai. Example: mylist.index(1, 11), yaha par(indexPossion, newValue)
7. pop(): Pop method thik append ka ulta hai. Ye by default list me last se ek value ko remove karta hai. Otherwise kisi specific index value ko remove karne ke liye is method me index postion dena hota hai. Example: mylist.pop() - Ye last se ek value remove kardega. mylist.pop(2) - Ye list ke 2nd index ki value ko remove kardega.
8. remove(): Remove ka use kiya jata hai jab aapko index postion ki jagh par value ka pata ho. To direct value ko remove karne ke liye remove method ka use karte hain. Example: mylist.remove(4) - Ye list me jaha bhi 4 hai useko remove karega.
9. reverse(): Reverse list ko ulta kardega. Means list by default assending order me hota hai. To ye list ko desending order me convert kar dega. Example: mylist.reverse()
10. sort(): Sort mehtod list ko assending order me sort kardega. Example: mylist.sort() yaha par sort(revers=Ture/False) Ture = Ye list ko desending order me sort karega. False = Ye assending order me sort karega.
11. count(): Count method list me present kisi bhi dublicate values ko count karne ke liye use hota hai. Example: mylist.count(4)
'''

firstClass = [1,2,3,4,5,6,7,8,9,10]
print('\nType: ', type(firstClass))
print('\nfirstclass: ', firstClass)

getSingleVlaue = firstClass[0]
print('\ngetSingleVlaue: ', getSingleVlaue)

# firstClass with names
myclass = ['Hey Sushil','Ram','Shyam','Radha','Seeta']
print('\nGet [0]: ', myclass[0])

# Put list in list
school = [firstClass, myclass]
print('\nschool: ', school)
print('\nGet firstclass form school: ', school[1])
print('\nGet myclass form school: ', school[1][0])
print('\nGet myclass form school: ', school[1][-1])

# list method
myclass = ['Hey Sushil','Ram','Shyam','Radha','Seeta']

# append()
myclass.append('YouTube Viewer')

# Direct override existing value by index posstion
myclass[1] = 'Shri Ram'

# find index postion using index()
findRollNumber = myclass.index('Shyam')
print('\nfindRollNumber: ', findRollNumber)

# existing index postion will get new value by insert()
myclass.insert(findRollNumber, 'Hanuman')

print('\nmyclass: ', myclass)

# copy() use to copy list
newclass = myclass.copy()

# user remove()
newclass.remove('Hey Sushil')

newclass.append('Old Student')

# pop() method use to remove by index postion
newclass.pop()

# new student
newstudent = ['Mona','Teena','Reena']

# extend()
newclass.extend(newstudent)

# find mona rollnumebr
findRollNumber = newclass.index('Mona')

newclass.pop(findRollNumber)



# clear()
myclass.clear()
print('\nmyclass: ', myclass)

# count()
newclass.append('Teena')
count = newclass.count('Teena')
print('\ncount: ', count)

otherclass = newclass.copy()

newclass.reverse()

otherclass.sort(reverse=True)

print('\nnewclass reverse: ', newclass)
print('\nnewclass sort: ', otherclass)

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