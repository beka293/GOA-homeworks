# 1) append მეთოდი ამატებს ელემენტს სიის ბოლოში.
# მაგალითი: list.append(5)

# 2) 
my_list = []
my_list.append(100)
my_list.append(200)
my_list.append(300)
my_list.append(400)
my_list.append(500)
print("დავალება 2:", my_list)

# 3) 
words = ["Python", "Java", "php"]
words.remove("Java")
print(" 3:", words)

# 4) remove(x) შლის მნიშვნელობით, pop(i) შლის ინდექსით და აბრუნებს ელემენტს.

# 5) 
nums = [21, 22, 23, 24, 25]
removed_item = nums.pop(-1)
print("ამოღებული:", removed_item)
print(" სია:", nums)

# 6) 
middle_list = [11, 2, 4, 22]
middle_list.insert(2, 3) 
print(" 6:", middle_list)

# 7)
sort_listt = [67, 68, 69, 70]
sort_listt.sort()
print(" 7:", sort_listt)

# 8) 
numberssss_rev = [1, 2, 3]
reversed_numbeeers = list(reversed(numberssss_rev))
print("8:", reversed_numbeeers)

# 9) 
wordssss_rev = ["ბოლო", "შუა", "თავი"]
result_rev = wordssss_rev[::-1]
print("9:", result_rev)

# 10) 
clear_list = [10, 20, 30]
clear_list = []
print(" 10:", clear_list)

# 11) 
index_list = [100, 200, 300]
pos = index_list.index(200)
print(" 11 (200-ის ინდექსი):", pos)

# 12) 
search_list = ["ვაშლი", "აფრიკოზი", "მანგო"]
user_word = "ვაშლი"
if user_word in search_list:
    print(f" ინდექსია {search_list.index(user_word)}")
else:
    print(" ვერ მოიძებნდა")

# 13) 
list_10 = []
for i in range(1, 11):
    list_10.append(i)
print(" 13:", list_10)

# 14) 
list_7 = [12, 5, 8, 22, 1, 14, 3]
print("მაქს:", max(list_7), "მინ:", min(list_7))

# 15) 
filtered_list = []

for i in range(10):
    n = int(input(f"შეიყვანეთ {i+1}-ე რიცხვი: "))
    
   
    if (n > 0 and n % 2 == 0): 
        filtered_list.append(n)
    elif (n < 0 and n % 2 != 0): 
        filtered_list.append(n)

if len(filtered_list) > 0:
    average = sum(filtered_list) / len(filtered_list)
    print("გაფილტრული სია:", filtered_list)
    print("ამ რიცხვების საშუალო:", average)
else:
    print("პირობა ვერცერთმა რიცხვმა ვერ დააკმაყოფილა.")