# mysql 
# sqlite3

# con ye connection ka alieas hai ya ek short name hai
import mysql.connector as con

# connection
# mydb = con.connect(host="localhost",user="root",password="")

# mydb ye mysql dabase connection ko hold kar rahakha hai.
mydb = con.connect(host="localhost",user="root",password="",database="moringpython")

print(mydb)

# creat new database
mycursor = mydb.cursor()

# query for creat dabase
# mysql.connector.connect(host="localhost",user="root",password="",database="moringpython").cursor().execute("CREATE DATABASE IF NOT EXISTS moringpython")

mycursor.execute("CREATE DATABASE IF NOT EXISTS moringpython")

# see database
mycursor.execute("SHOW DATABASES")

for d in mycursor:    
    print(d)

# create new user table
mycursor.execute("CREATE TABLE IF NOT EXISTS newtable(id int(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, fname VARCHAR(50) NOT NULL, lname VARCHAR(50), mobile INT(10))")

# shwo table
mycursor.execute("SHOW TABLES")
for t in mycursor:
    print("Table: ",t)

# insert data in table
fname = input('Enter first name: ')
lname = input('Enter last name: ')
mobile = int(input('Enter your mobile: '))

insertData = "INSERT INTO user(fname, lname, mobile) VALUES('{}','{}','{}')".format(fname,lname,mobile)

mycursor.execute(insertData)
# for insert value in table use commit method
mydb.commit()

# confirm insert recor
print(mycursor.rowcount, "recorded inserted")

# get table data by select
# mycursor.execute("SELECT * FROM user")
# mycursor.execute("SELECT fname,mobile FROM user")

# searchdata = input('Enter your data: ')
# useing where
# data = "SELECT fname,mobile FROM user WHERE fname='{}'".format(searchdata)

# get data orderby
# data = "SELECT fname,mobile FROM user ORDER BY id DESC"

# limited data`
data = "SELECT fname,mobile FROM user ORDER BY id DESC LIMIT 10"
mycursor.execute(data)
getTableData = mycursor.fetchall()

for tdata in getTableData:
    # print('Name: ',tdata[0],' Mobile: ',tdata[1])
    print(tdata)

# dete data form table
detelQuery = "DELETE FROM user WHERE id=1"
mycursor.execute(detelQuery)
mydb.commit()
print(mycursor.rowcount, 'record delted')


# delete table
mycursor.execute("DROP TABLE IF EXISTS newtable")

# UPDATE TABLE DATA
updateQuery = "UPDATE user SET fname='Ram Kumar' WHERE id=10"
mycursor.execute(updateQuery)
mydb.commit()
print(mycursor.rowcount, 'Recored chaned')


'''
1. connect library ko install karna
2. con lib ke method connect ka use karke connection create karna
3. connection time pe 4 values cahiye host/user/password aur jab conneciton create ho gaya tab database banae ke bad 4th arguemtn database name yaha pass karna hoga
4. database query ko run karne ke liye excute method chaaiye jo ki ek new variable mycurse me store kar liye
5. jab table me insert/update/delete karna hoga tab mydb means connection variable ke method commit() ko call karna hoga. taki table me update/inser ya delete kiya ja sakte
'''

# Table joining

# craete user subject table
mycursor.execute("CREATE TABLE IF NOT EXISTS subject(id int(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, hindi INT(4), english INT(4), math INT(4), user_id INT(10))")

# get subject marsk by teacher
h = int(input('Enter Hindi marks: '))
e = int(input('Enter English marks: '))
m = int(input('Enter Math marks: '))
ui = int(input('Enter student roll number: '))

insertData = "INSERT INTO subject(hindi, english, math, user_id) VALUES('{}','{}','{}','{}')".format(h, e, m, ui)

mycursor.execute(insertData)
# for insert value in table use commit method
mydb.commit()


# joint user and subject table
# inner joing / left joing / right joining

'''
inner join: comman data form both table
left join: get left table all data 
right join: get right table all data 
'''
# inner join without table alias

# tablesql = "SELECT \
# user.*, subject.* FROM user \
# INNER JOIN subject ON user.id = subject.user_id"

# inner joint with table sort names

# tablesql = "SELECT \
# u.fname,u.mobile, s.hindi,s.english,s.math FROM user AS u \
# INNER JOIN subject AS s ON u.id = s.user_id"

# left join

# tablesql = "SELECT \
# u.fname,u.mobile, s.hindi,s.english,s.math FROM user AS u \
# LEFT JOIN subject AS s ON u.id = s.user_id"

# right join

tablesql = "SELECT \
u.fname,u.mobile, s.hindi,s.english,s.math FROM user AS u \
RIGHT JOIN subject AS s ON u.id = s.user_id"

mycursor.execute(tablesql)

gettableData = mycursor.fetchall()

print('''
    ------------------------------------
    Name    Mobile  Hindi   English Math
    ------------------------------------
''')
for tus in gettableData:
    print('''
    
    {}      {}      {}      {}      {}
    '''.format(tus[0],tus[1],tus[2],tus[3],tus[4]))
