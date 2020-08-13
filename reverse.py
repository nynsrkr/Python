number=int(input("Enter the number you want to reverse "))
reverse=0
while(number>0):
    last=number%10
    reverse=(reverse*10)+last
    number=number//10
string=str(reverse)
print("The reversed number is "+string)
