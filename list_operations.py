#change values in list

cars=['maruti','honda','bmw','fiat']

print(cars)

cars[0]='porsche'

print(cars)

#adding element to list to end of list

cars.append('hyundai')

print(cars)


#adding names to empty list
names=[]

names.append('Nayan')
names.append('Ram')
names.append('Rahul')
names.append('Tom')
print(names)
names.insert(1,'James')
print(names)

#removing elements from list with index specified

del names[1]
print(names)

#removing elements from end of list , popping
remover=names.pop()
print(remover)


#popping elements from any position in list
hello=names.pop(0)
print('My Name is'+hello.upper())

names.remove('Ram') #remove item from list when position not known
print(names)
