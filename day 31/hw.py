# 1
text = "   გამარჯობა სამყარო   "
cleaned_text = text.strip()
print(cleaned_text)

# 2
name = input("შემოიტანეთ სახელი: ").strip()
print(name)

# 3
word = input("შემოიტანეთ სიტყვა: ")
print(word.startswith("A"))

# 4
website = input("შემოიტანეთ ვებსაიტი: ")
print(website.startswith("https"))

# 5
filename = input("შემოიტანეთ ფაილის სახელი: ")
print(filename.endswith(".py"))

# 6
email = input("შემოიტანეთ ელფოსტა: ")
print(email.endswith("@gmail.com"))

# 7
text = "The horse is sleeping. I love my horse."
new_text = text.replace("horse", "cat")
print(new_text)

# 8
sentence = input("შემოიტანეთ წინადადება: ")
new_sentence = sentence.replace(" ", "-")
print(new_sentence)

# 9
phone = input("შემოიტანეთ ნომერი: ")
clean_phone = phone.replace("-", "")
print(clean_phone)

# 10
text = input("შემოიტანეთ ტექსტი: ").strip()
print(text.startswith("salami"))

# 11
password = input("შემოიტანეთ პაროლი: ")
starts_with_upper = password[0].isupper() 
ends_with_one = password.endswith("1")
print("იწყება დიდი ასოთი:", starts_with_upper)
print("მთავრდება 1-იანით:", ends_with_one)

# 12
sentence = input("შემოიტანეთ წინადადება: ").strip()
if not sentence.endswith("."):
    sentence = sentence + "."
formatted_sentence = sentence.replace(" ", "_")
print(formatted_sentence)

# 13
full_name = input("შემოიტანეთ სრული სახელი (სახელი გვარი მამის სახელი): ")
parts = full_name.split()
print("სახელის ნაწილები:", parts)
print("სიტყვების რაოდენობა:", len(parts))

# 14
sentence = input("შემოიტანეთ წინადადება: ")
words = sentence.split()

longest = words[0]
shortest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word
    if len(word) < len(shortest):
        shortest = word

print("ყველაზე გრძელი:", longest)
print("ყველაზე მოკლე:", shortest)
# 15

numbers_string = input("შემოიტანეთ რიცხვები (მაგ: 67 52 1488 69 42): ")

numbers_list = []
for x in numbers_string.split():
    numbers_list.append(int(x))

print("რიცხვების სია:", numbers_list)
print("ჯამი:", sum(numbers_list))
print("ყველაზე დიდი:", max(numbers_list))
print("ყველაზე პატარა:", min(numbers_list))