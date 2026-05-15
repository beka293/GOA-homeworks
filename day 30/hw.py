# 1 and 2
upper_text = "პითონი საინტერესო პროგრამირების ენაა"
lower_result = upper_text.lower()
print(f"2) პატარა ასოებით: {lower_result}")

# 3 and 4
user_word = input("4) შემოიტანეთ სიტყვა (გადასადიდებლად): ")
print(f"შედეგი: {user_word.upper()}")

# 5 and 6
words_list = ["apple", "banana", "cherry"]
print("6) სიის ელემენტები title ფორმატში:")
for word in words_list:
    print(word.title())

# 7
mixed_str = "PyThOn 3.10"
print(f"7) swapcase შედეგი: {mixed_str.swapcase()}")

# 8
static_text = "პროგრამირება"
print(f"8) ასო 'რ' გვხვდება {static_text.count('რ')}-ჯერ სიტყვაში '{static_text}'")

# 9
user_sentence = input("9) შემოიტანეთ წინადადება: ")
user_symbol = input("შემოიტანეთ საძიებო სიმბოლო: ")
print(f"სიმბოლო '{user_symbol}' გვხვდება {user_sentence.count(user_symbol)}-ჯერ")

# 10
fname = input("10) შემოიტანეთ სახელი: ")
lname = input("შემოიტანეთ გვარი: ")
print(f"სწორი ფორმატი: {fname.title()} {lname.title()}")

# 11
vowel_text = input("11) შემოიტანეთ წინადადება ხმოვნების დასათვლელად: ")
vowels = "aeiouAEIOUაეიოუ"
v_count = 0
for symbol in vowel_text:
    if symbol in vowels:
        v_count += 1
print(f"ხმოვნების რაოდენობაა: {v_count}")

# 12
stat_text = input("12) შემოიტანეთ წინადადება სტატისტიკისთვის: ")
length = len(stat_text)

if length > 0:
    v_list = "aeiouAEIOUაეიოუ"
    c_list = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZბგდვზთკლმნპჟრსტფქღყშჩცძწჭხჯჰ"
    
    u_cnt = 0
    l_cnt = 0
    v_cnt = 0
    c_cnt = 0
    s_cnt = stat_text.count(" ")

    for symbol in stat_text:
        if symbol.isupper(): u_cnt += 1
        if symbol.islower(): l_cnt += 1
        if symbol in v_list: v_cnt += 1
        if symbol in c_list: c_cnt += 1

    print(f"--- სტატისტიკა ---")
    print(f"დიდი ასოები: {(u_cnt/length)*100:.1f}%")
    print(f"პატარა ასოები: {(l_cnt/length)*100:.1f}%")
    print(f"ხმოვნები: {(v_cnt/length)*100:.1f}%")
    print(f"თანხმოვნები: {(c_cnt/length)*100:.1f}%")
    print(f"სფეისები: {(s_cnt/length)*100:.1f}%")
else:
    print("ტექსტი არ არის შეყვანილი.")