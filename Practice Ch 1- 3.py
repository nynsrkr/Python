#Store a message in a variable, and print that message Then change the value of your variable to a new message, and print the new message
message="How are you today"
print(message)
message="Where do you want to go today?"
print(message)

#2-3. Personal Message: Store a person’s name in a variable, and print a message to that person Your message should be simple, such as, “Hello Eric,would you like to learn some Python today?”
name="eric"
print("Hello "+name.title()+", would you like to learn some Python today?")

#2-4. Name Cases: Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase
name="nayan"
print(name.title())
print(name.upper())
print(name.lower())

#2-7. Stripping Names: Store a person’s name, and include some whitespace
#characters at the beginning and end of the name Make sure you use each
#character combination, "\t" and "\n", at least once
name="Shyam" #revise this
print("\n\t"+name)

#Print the name once, so the whitespace around the name is displayed
#Then print the name using each of the three stripping functions, lstrip(),
#rstrip(), and strip()
new_name="                James                "
print(new_name.lstrip())
print(new_name.rstrip())
print(new_name.strip())

# create a list , #print list

cars=[]
cars.append('maruti')
cars.append('bmw')
cars.append('sx4')
cars.append('honda')
cars.append('fiat')
print(cars)


#print particular values in a list

print(cars[3]) #will print honda

#concantenate list variable with string

print("This was my last car, "+cars[2])


#print particular variable at reverse index in list
print(cars[-2]) #will print honda

#apply methods such as title,upper,lower, left and right blank strip

print(cars[3].upper())
print(cars[3].title())
print(cars[3].lower())

#change values in list at index

cars[3]='jazz'
print(cars)

#add values in list

cars.append('Mercedes')
print(cars)

#add value in list at index  #REVISE THIS
cars.insert(3,"Hyundai")
print(cars[3])

#delete values in list
del cars[1]
print(cars)

#replace value in list when position not know read page 78 #REVISE
cars.remove("fiat")
print(cars)

#store and print or run methods on popped variables
remover=cars.pop()
print(remover.upper())
print(remover.lower())
#store and print or run methods on specific popped variable
remover2=cars.pop(2)
print("This variable was removed"+remover2)
