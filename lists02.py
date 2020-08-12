#Store a message in a variable, and print that message Then change the value of your variable to a new message, and print the new message
name="Nayan"
print(name)
name="Nayan Sarkar"
print(name)

#2-3. Personal Message: Store a person’s name in a variable, and print a message to that person Your message should be simple, such as, “Hello Eric,would you like to learn some Python today?”
print("How are you doing today, "+name+"?")

#2-4. Name Cases: Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase
print(name.upper())
print(name.lower())
print(name.title())

#2-7. Stripping Names: Store a person’s name, and include some whitespace
#characters at the beginning and end of the name Make sure you use each
#character combination, "\t" and "\n", at least once
print("\n\tHow are you today")

#Print the name once, so the whitespace around the name is displayed
#Then print the name using each of the three stripping functions, lstrip(),
#rstrip(), and strip()
name="               Nayan                "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

# create a list , #print list
cars=['honda','mercedes','suzuki','ford','fiat']
print(cars)

#print particular values in a list
print(cars[2]) #will print suzuki

#concantenate list variable with string

print("This is my car"+cars[2].upper())


#print particular variable at reverse index in list
print(cars[-2]) #will print ford

#apply methods such as title,upper,lower, left and right blank strip
print(cars[3].upper())

#replace values in list at index
cars[2]='suzuki replaced by hyundai'
print(cars)

#add values in list

cars.append('maruti')
print(cars)

#add value in list at index  #REVISE THIS

cars.insert(1,"mercedes replaced by bmw")
print(cars)

#delete values in list
del cars[3]
print(cars)

#remove value in list when position not know read page 78 #REVISE
cars.remove('honda')

#store and print or run methods on popped variables

#store and print or run methods on specific popped variable

#use the remove() method to work with a value that’s being removed from a list.
rem='fiat'
cars.remove(rem)
print(rem.upper())
