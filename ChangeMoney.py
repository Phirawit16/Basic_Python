#change money

#input
from sre_constants import JUMP


Money = int(input("How many money => "))

#process
if Money >= 1000 :
    Dev_Thou = Money // 1000 #ส่วนจาก1000
    Money = Money - ( Dev_Thou * 1000 ) #เหลือจาก1000
    print("จำนวนแบงค์พัน = ", Dev_Thou)

if Money >=500 :
    Dev_FiveHund = Money // 500 #ส่วนจาก500
    Money = Money - ( Dev_FiveHund * 500 ) #เหลือจาก500
    print("จำนวนแบงค์ห้าร้อย = ", Dev_FiveHund)

if Money >=100 :
    Dev_Hund = Money // 100 #ส่วนจาก100
    Money = Money - ( Dev_Hund * 100 ) #เหลือจาก100
    print("จำนวนแบงค์ร้อย = ", Dev_Hund)

if Money >=50 :
    Dev_Fif = Money // 50 #ส่วนจาก50
    Money = Money - ( Dev_Fif * 50 ) #เหลือจาก100
    print("จำนวนแบงค์ห้าสิบ = ", Dev_Fif)

if Money >=20 :
    Dev_Twen = Money // 20 #ส่วนจาก20
    Money = Money - ( Dev_Twen * 20 ) #เหลือจาก20
    print("จำนวนแบงค์ยี่สิบ = ", Dev_Twen)

if Money >=10 :
    Dev_Ten = Money // 10 #ส่วนจาก10
    Money = Money - ( Dev_Ten * 10 ) #เหลือจาก10
    print("จำนวนเหรียญ์สิบ = ", Dev_Ten)

if Money >0 :
    Left_one = Money #เหลือจาก1
    print("จำนวนเหรียญบาท = ", Left_one)
