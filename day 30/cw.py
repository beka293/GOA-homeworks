text = input("შეიყვანეთ ტექსტი: ")

upper = 0
lower = 0


for i in text:
   
    if i.lower() != i.upper():
        if i != i.lower(): 
            upper = upper + 1
        elif i != i.upper():
            lower = lower + 1

print("დიდი ასოები:", upper)
print("პატარა ასოები:", lower)