name = input(" Please tell your name => " ) #Input() is used for get input from user
lname = input("Please tell your last name => ") 
age = input(" Plaese tell your age => ")
print("Your name is = " + name +"\t"+ lname)
print("Age = " + age)

#Input() is used for get input from user
#Input() is get the STRING type 
''' Beware to convert string into another before use'''

x = input("Number 1 = ")
y = input("Number 2 = ")
print( "Answer => " + str( int(x) + int(y) ) )

''' Get input as String and convert at Print '''

#OR

''' Get input as Integer '''

x = int(input("First Number => "))
y = int(input("Second Number => "))
print( "Answer is "+ str( x + y ) )
