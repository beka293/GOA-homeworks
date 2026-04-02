for i in range(0, 101):  
    print(i)


for i in range(40, 251):
    if i % 2 == 0:
        print(i)


for i in range(200, 401):
    if i % 5 == 0 and i % 4 == 0:
        print(i)

n = int(input("შეიყვანეთ რიცხვი: "))
for i in range(2, n + 1):
    print(i)


    n = int(input("შეიყვანეთ რიცხვი: "))
for i in range(n, -1, -1):
    print(i)


number = 42

while True:
    guess = int(input("გამოიცანი რიცხვი: "))
    
    if guess == number:
        print("სწორია! რიცხვი იყო", number)
        break
    elif guess < number:
        print("ნაკლებია, სცადე უფრო დიდი რიცხვი")
    else:
        print("მეტია, სცადე უფრო პატარა რიცხვი")
