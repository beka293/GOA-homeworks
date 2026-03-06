temp = float(input("შეიტანე ტემპერატურა: "))
rain = input("წვიმაა? (yes/no): ").lower()
if temp > 25 and rain == "no":
    print("შესანიშნავი ამინდია სასეირნოდ!")
elif temp > 25 and rain == "yes":
    print("ცხელი და წვიმიანია, ჩაფხუტი დაგჭირდება!")
elif temp < 10 or rain == "yes":
    print("სჯობს სახლში დარჩე")
else:
    print("სასიამოვნო ამინდია")

