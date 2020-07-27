# regex:

'''
Regex module:

'''

import re

name = "Ram kumar singh"
searchname = re.search("^Ram.*singh$", name)
print('serachname: ',searchname)

'''
Regex fuction:

1. findall(): 
2. search()
3. split()
4. sub()


Regex Metachar:

[] => set of char: [a-zA-Z]
\ => \d \f \n
. => r...m
^ => start with
$ => end with
* => zero or more occurance 
+ => one or more
{} => exactly numer of occurencse
| => eiter or
() => capture and group


Special Sequences:

\A => return begning char \ARam
\b => return at befining or ending
\B =>  returns a match where the specifed char are present
\d => find digit(0-9)
\D => ram001
\s => return stirng ram kumar singh
\S => return where sting not have space
\w => return if have string digit underscore
\W => sting does not contain any word char
\Z => return at last or end srting


Sets:

[arn]
[a-n]
[^arn]
[0123]
[0-9]
[0-5][0-9] => 00,02
[a-zA-Z]
[+] => +,*,.,|,(),$,{}
'''

# practice: findall()
message = "This is monday and great day."
search = re.findall('Ram', message)
print(search)

# search()
aserach = re.search("monday",message)
print('aserach: ',aserach)


# split()
splitmessage = re.split('a',message)
print('splitmessage: ',splitmessage)

splitmessage = re.split(' ',message, 1)
print('splitmessage max: ',splitmessage)

# sub()
replace = re.sub('This', 'July', message)
print('replace: ',replace)

