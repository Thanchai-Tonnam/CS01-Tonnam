A = int(input("ใส่ตัวเลข : "))
count = 0
for number in range(A):
    if number % 2 == 1:
        count += 1
        print(number)