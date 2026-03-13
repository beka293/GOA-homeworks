weight = float(input("წონა (კგ): "))
height = float(input("სიმაღლე (მ): "))
age = int(input("ასაკი: "))

BMI = weight / (height * height)

if BMI < 18.5 and age >= 18:
    print("შენი BMI დაბალია")
    print("შესაძლოა წონის მომატება დაგჭირდეს")
elif BMI >= 18.5 and BMI <= 24.9 and age >= 18:
    print("შენი BMI ნორმალურია")
    print("ჯანმრთელ ფორმაში ხარ")
elif BMI >= 25 and BMI < 30 or age < 18:
    print("BMI საშუალოზე მაღალია")
    print("ჯანსაღი კვება მნიშვნელოვანია")
elif BMI >= 30:
    print("BMI მაღალია")
    print("სასურველია ექიმთან კონსულტაცია")
else:
    print("მონაცემები ვერ დამუშავდა")
    print("სცადე თავიდან")
