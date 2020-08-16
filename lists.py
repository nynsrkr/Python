#Store a message in a variable, and print that message Then change the value of your variable to a new message, and print the new message
message="How are you today"
print(message)
message="This is message 2"
print(message)

#2-3. Personal Message: Store a person’s name in a variable, and print a message to that person Your message should be simple, such as, “Hello Eric,would you like to learn some Python today?”
name="nayan"
print("How are you today, "+name)

#2-4. Name Cases: Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase
print(name.upper())
print(name.lower())
print(name.title())

#2-7. Stripping Names: Store a person’s name, and include some whitespace
#characters at the beginning and end of the name Make sure you use each
#character combination, "\t" and "\n", at least once
names="\n\thello world"
print(names)


#Print the name once, so the whitespace around the name is displayed
#Then print the name using each of the three stripping functions, lstrip(),
#rstrip(), and strip()
new_name="                Nayan           "
print(new_name)
print(new_name.lstrip())
print(new_name.rstrip())
print(new_name.strip())

# create a list , #print list
list=['honda','bmw','suzuki']
print(list)

#print particular values in a list
print(list[1])
print(list[1].upper())

#concantenate list variable with string
print("This is my new car "+list[1].upper())

#print particular variable at reverse index in list
print(list[-1])

#apply methods such as title,upper,lower, left and right blank strip


#replace values in list at index
list[2]="subaru"
print(list)

#add values in list
list.append('mercedes')
print(list)

#add value in list at index  #REVISE THIS
list.insert(1,"hyundai")
print(list)

#delete values in list
del list[2]
print(list)

#remove value in list when position not know read page 78 #REVISE
list.remove("hyundai")
print(list)

#store and print or run methods on popped variables
var=list.pop()
print(list)
print('This variable was removed '+var.upper())

#store and print or run methods on specific popped variable
list.append('sx4')
list.append('fiat')
print(list)
hello=list.pop(1)
print('This variable was popped '+hello)