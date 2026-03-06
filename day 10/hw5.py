username = input("შეიტანე მომხმარებლის სახელი: ")
password = input("შეიტანე პაროლი: ")
if username == "admin" and password == "superSecretPassword":
    print("მოგესალმები, ადმინ!")
elif username == "guest" and password == "1234":
    print("მოგესალმები, სტუმარო!")
else:
    print("მომხმარებელი არ მოიძებნა!")