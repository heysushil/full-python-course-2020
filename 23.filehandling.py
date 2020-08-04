# filhandling
# creat / open / read / write / delte / close
'''
open()
r = read
a = create / read
w = write
x = create / write

t = text
b = binary / muldi media files image
'''

demofile = open('C:/xampp/htdocs/htmldemo/full-python-course-2020/demo.txt','r')
# print('\n\n',demofile.read())

# read speicific part of file
print('\n',demofile.read())

# file write
writeFile = open('C:/xampp/htdocs/htmldemo/full-python-course-2020/demo.txt','a')

writeFile.write('\nHello New python version 3.0')
writeFile.close()


# creat new file x/a/w
# creatNewFile = open('C:/xampp/htdocs/htmldemo/full-python-course-2020/vivek.txt','w')

# delete a file
import os
deleteFile = os.remove('C:/xampp/htdocs/htmldemo/full-python-course-2020/vivek.txt')
if deleteFile == None:
    print('File delte successfully')
else:
    print('File not exists')

