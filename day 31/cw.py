# sentence = input("წინადადება: ").strip()
# word = input("სიტყვა: ").strip()

# print(sentence.startswith(word))

# sentence = input("წინადადება: ").strip()
# word = input("სიტყვა: ").strip()

# print(sentence.endswith(word))

# colors_input = input("ჩამოთვალეთ თქვენი საყვარელი ფერები: ")

# colors_list = colors_input.split()

# print(colors_list)


numbers_input = input("შემოიტანეთ რიცხვები: ")

string_list = numbers_input.split()

numbers_list = []

for i in string_list:
    numbers_list.append(int(i))

print(numbers_list)