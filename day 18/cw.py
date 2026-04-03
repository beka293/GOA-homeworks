n = int(input("შეიყვანეთ რიცხვი: "))
if n % 2 == 0:
    print(f"{n} რიცხვი ლუწია")
else:
    print(f"{n} რიცხვი კენტია")


for n in range(1, 101):
    if n % 2 == 0:
        print(f'{n} ლუწია')
    else:
        print(f'{n} კენტია')