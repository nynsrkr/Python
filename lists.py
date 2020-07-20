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
