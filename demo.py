numberoffriends = int(input('Enter number of friends to add on list: '))
friendlist = []
i =  0
while i < numberoffriends:
    name = input('\nEnter friedn name: ')
    friendlist.append(name)
    i += 1

print(friendlist)