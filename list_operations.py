#TRY it yourself exercises page 40

#3-1 Names

names=['nayan','rahul','ganesh','ram']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# 3-2 Greetings
print("How are you today,"+names[0].title()+"?")
print("How are you today,"+names[1].title()+"?")
print("How are you today,"+names[2].title()+"?")
print("How are you today,"+names[3].title()+"?")

#3-3 Your own list
cars=['bmw','ford','honda','suzuki','tesla','fiat','porsche']
print(cars) #will print all elements in list

print(cars[0]) #will print element at index 0

print(cars[2]) #will print element at index 2

print(cars[2].upper()) #method upper applied to cars index 2

hello=cars[0] # element at index 0 in list cars is stored in variable hello

apples=cars[-1] #last element in list is stored in variable apples

print(hello+" "+apples) #concatenation of variables

print("My first car was a "+cars[0].upper()) #using individual elements from list

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

print('Hello World')
