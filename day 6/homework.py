#მონაცემთა ტიპები პროგრამირებაში საშუალებას გვაძლევს შევინახოთ და დავამუშაობოთ სხვადასხვა სახის ინფორმაცია ეფექტურად.
# მრავალი ტიპის არსებობა უზრუნველყოფს მეხსიერების ოპტიმიზაციას და ოპერაციების სწორ შესრულებას.

#num2 შეყვანის მოწყობილობები, როგორიცაა კლავიატურები, მაუსები და მიკროფონები, საშუალებას აძლევს მომხმარებლებს, გაგზავნონ მონაცემები და ბრძანებები კომპიუტერულ სისტემაში.
#  გამომავალი მოწყობილობები, მათ შორის მონიტორები, პრინტერები და დინამიკები, დამუშავებულ ინფორმაციას მომხმარებელს უბრუნებენ.


#num3
name = "სახელი"  # str
age = 25         # int
height = 1.75    # float
print(type(name))   # class 'str'
print(type(age))    # class 'int'
print(type(height)) # class 'float'


#num4
distance_km = float(input("შეიტანეთ მანძილი კილომეტრებში: "))
distance_m = distance_km * 1000

print("მანძილი მეტრებში:", distance_m )


#num5
num1 = int(input("Enter Your age: "))
num2 = int(input("Enter Your height: "))
print("მიმატება: ", num1 + num2)
print("გამოკლება: ", num1 - num2)
print("გამრავლება: ", num1 * num2)
print("გაყოფა: ", num1 / num2)

#num6
weight = float(input("შეიტანეთ წონა კგ-ში: "))
height = float(input("შეიტანეთ სიმაღლე მეტრებში: "))
bmi = weight / (height * height)
print("თქვენი BMI: ", bmi)
