# mysql 
# sqlite3
import mysql.connector as con

# connection
mydb = con.connect(host="localhost",user="root",password="", database="moringpython")
print(mydb)

# creat new database
mycursor = mydb.cursor()

# query for creat dabase
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

# limited data
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


