# text = input("შეიყვანეთ ტექსტი: ")
# n = len(text)
# print(f"თქვენს ტექსტში {n} სიმბოლოა")

# text = input("შეიყვანეთ ტექსტი")
# count = text.count('n')

# if count == 0:
#     print("თქვენს ტექსტში ასო n არ არის")
# else:
#     print("თქვენს ტექსტში ასო n", count, "ჯერ გამოდის")



numbers = [12, 7.5, 9, 4.2, 15, 20, 3.0, 8]


for num in numbers:
    if num % 3 == 0:
        print(num)

        

numbers = [12, 7.5, 9, 4.2, 15, 20, 3.0, 8, 6.0]


for i in range(len(numbers)):
    num = numbers[i] 
    if num % 3 == 0:
        print("3-ზე იყოფა:", num)