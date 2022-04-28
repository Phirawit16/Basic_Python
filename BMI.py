#BMI = weight (kg) / height^2 (m)

#input / convert to integer
height = int(input("insert your height (cm) => "))
weight = int(input("insert your weight (kg) => "))

# cm => m
height /= 100

#calcilate BMI
BMI = weight / (height**2)

#output
print("Your BMI => ", BMI)

''' BMI 
    น้อยกว่า 18.50          น้ำหนักน้อย / ผอม	มากกว่าคนปกติ
    ระหว่าง 18.50 - 22.90	ปกติ (สุขภาพดี)	เท่าคนปกติ
    ระหว่าง 23 - 24.90	    ท้วม / โรคอ้วนระดับ 1	อันตรายระดับ 1
    ระหว่าง 25 - 29.90	    อ้วน / โรคอ้วนระดับ 2	อันตรายระดับ 2
    มากกว่า 30	            อ้วนมาก / โรคอ้วนระดับ 3	อันตรายระดับ 3 '''

if BMI<18.50 :
    print("ผอม", BMI<18.50)

elif 18.50<BMI and BMI<22.90:
    print("ปกติ", 18.50<BMI and BMI<22.90)

elif 23<BMI and BMI>24.90 :
    print("อ้วนระดับ 1", 23<BMI and BMI>24.90)

elif 25<BMI and BMI>29.90 :
    print("อ้วนระดับ 2", 25<BMI and BMI>29.90)

elif BMI>30 :
    print("อ้วนระดับ 3", BMI>30)

else :
    print(" WTF ")