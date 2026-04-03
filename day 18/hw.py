for i in range(200, 501):
    if i % 4 == 0 or i % 7 == 0:
        print(i)



i = 200
while i <= 500:
    if i % 4 == 0 or i % 7 == 0:
        print(i)
    i += 1


#2
for i in range(300, 1001):
    if i % 3 == 0 or i % 10 == 0:
        print(i)


i = 300
while i <= 1000:
    if i % 3 == 0 or i % 10 == 0:
        print(i)
    i += 1


#3
for i in range(1, 51):
    if i % 2 == 0:
        print(f"Even: {i}")
    else:
        print(f"Odd: {i}")


#4
positive = 0
negative = 0
for _ in range(10):
    num = float(input("შეიტანეთ რიცხვი: "))
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
print(f"დადებითი: {positive}")
print(f"უარყოფითი: {negative}")


#5
num = int(input("შეიტანეთ რიცხვი: "))
if num % 2 == 0 and num % 3 == 0:
    print("Good")
elif num % 2 == 0:
    print("Two")
elif num % 3 == 0:
    print("Three")
else:
    print("None")

#6
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


#7
positive = 0
negative = 0
while True:
    num = float(input("შეიტანეთ რიცხვი (0-ით შეწყვიტე): "))
    if num == 0:
        break
    elif num > 0:
        positive += 1
    else:
        negative += 1
print(f"დადებითი: {positive}")
print(f"უარყოფითი: {negative}")


#8
n = int(input("შეიტანეთ რიცხვი: "))
for i in range(1, n + 1):
    if i % 4 != 0:
        print(i)



#9
for _ in range(5):
    num = int(input("შეიტანეთ რიცხვი: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")




count = 0
while count < 5:
    num = int(input("შეიტანეთ რიცხვი: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
    count += 1