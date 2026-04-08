for i in range(100, 401):
    if i % 5 == 0 and i % 3 != 0:
        print(i)


i = 100
while i <= 400:
    if i % 5 == 0 and i % 3 != 0:
        print(i)
    i += 1


#2
for i in range(1, 101):
    if i % 2 == 0 and i % 5 == 0:
        print("EvenFive")
    elif i % 2 == 0:
        print("Even")
    elif i % 5 == 0:
        print("Five")
    else:
        print(i)

#3
max_num = float('-inf')
min_num = float('inf')
for _ in range(8):
    num = float(input("შეიტანეთ რიცხვი: "))
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
print(f"მაქსიმუმი: {max_num}")
print(f"მინიმუმი: {min_num}")


#4
n = int(input("შეიტანეთ N: "))
count = 0
for i in range(1, n + 1):
    if i % 3 == 0:
        count += 1
print(f"3-ის ჯერადები: {count}")

#5
for i in range(1, 51):
    if i % 4 != 0:
        print(i)

#6
total = 0
while True:
    num = float(input("შეიტანეთ რიცხვი (უარყოფითი გასაჩერებლად): "))
    if num < 0:
        break
    total += num
print(f"ჯამი: {total}")

#7
