
# my_list = ["Apple", 10, "Python", 3.14, True]
# print( my_list)

# print(my_list.pop())



რაოდენობა = int(input("რამდენი ელემენტი გინდა? "))

s = []

for i in range(რაოდენობა):
    მონაცემი = input(f"შეიყვანე {i+1}-ე რამე: ")
    s = s + [მონაცემი]
print("შენი სიაა:", s)