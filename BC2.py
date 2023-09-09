tt = 0
for i in range(10):
    num = int(input("Num:  "))
    if num < 0:
        continue
    tt += num
print("ผลรวมของตัวเลขที่ไม่ใช่เลขลบคือ:", tt)