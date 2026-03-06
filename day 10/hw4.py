age = int(input("შეიტანე შენი ასაკი: "))
student = input("სტუდენტი ხარ? (yes/no): ")
if age < 12 or age > 65:
    print("ბილეთი უფასოა")
elif student == "yes" and age > 12:
    print("ბილეთი ნახევარ ფასად")
else:
    print("სრული ფასი უნდა გადაიხადო")
