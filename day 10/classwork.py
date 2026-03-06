
asaki = int(input("შეიტანე შენი ასაკი: "))
student_status = input("შენ სტუდენტი ხარ? (დიახ/არა): ")


adult = asaki >= 18


is_student = student_status == "დიახ"

print(adult and is_student)
