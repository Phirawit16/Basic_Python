name = input("Insert Your name => ")
age = int(input("Insert Your Age => "))

''' if boolean expression :
        statement             '''

if age > 0 and age < 15 :
    print("เด็กชาย " + name)
elif age >=15 : 
    print("นาย " + name)
else :
    print("มึงเป็นคนเปล่าหนิ")

#Another way to write If...else

print("คน") if age > 0 and age <= 100 else print("มึงเป็นคนเปล่าหนิ")