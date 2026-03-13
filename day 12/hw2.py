age = int(input("ასაკი: "))
license = input("მართვის მოწმობა (yes/no): ")
drunk = input("ალკოჰოლის ზემოქმედება (yes/no): ")

if age >= 18 and license == "yes" and drunk == "no":
    print("შეგიძლია მანქანის მართვა")
    print("უსაფრთხო მგზავრობას გისურვებთ")
elif age >= 18 and license == "no" and drunk == "no":
    print("ასაკი საკმარისია")
    print("მაგრამ მართვის მოწმობა არ გაქვს")
elif drunk == "yes" or age < 18 or license == "no":
    print("მანქანის მართვა აკრძალულია")
    print("ეს შეიძლება საშიში იყოს")
else:
    print("მონაცემები ვერ გადამოწმდა")
    print("სცადე თავიდან")
