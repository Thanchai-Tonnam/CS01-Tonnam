print("โปรแกรมประมวลผลเกรด")
inp_work = int(input("คะแนนงาน = "))
inp_mid = int(input("คะแนนกลางภาค = "))
inp_final = int(input("คะแนนปลายภาค = "))
GS = inp_work + inp_mid + inp_final
if GS >= 80:
    print("Grade A")
elif GS >= 75:
    print("Grade B+")
elif GS >= 70:
    print("Grade B")
elif GS >= 65:
    print("Grade C+")
elif GS >= 60:
    print("Grade C")
elif GS >= 55:
    print("Grade D+")
elif GS >= 50:
    print("Grade D")
elif GS <= 40:
    print("Grade F")
else:
    print("ไม่พบข้อมูล")
