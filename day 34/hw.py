#1  ფუნქცია არის კოდის იზოლირებული, წინასწარ გამზადებული „პატარა მანქანა“ ან ბლოკი, რომელსაც აქვს თავისი სახელი და ასრულებს კონკრეტულ დავალებას.
#2 კოდის მრავალჯერადი გამოყენება (Reusability): თუ ერთი და იგივე მოქმედება კოდის სხვადასხვა ადგილას გვჭირდება, კოდს რამდენჯერმე კი არ ვწერთ, არამედ ერთხელ ვქმნით ფუნქციას და შემდეგ მას ვიძახებთ.

# კოდის წაკითხვადობა და ორგანიზება: კოდი ხდება უფრო სუფთა, სტრუქტურირებული და მარტივად გასაგები როგორც ჩვენთვის, ისე სხვა დეველოპერებისთვის.

# მარტივი ტესტირება და განახლება (Maintenance): თუ კოდში რაიმე შეცდომაა ან რამის შეცვლა გვინდა, ცვლილებას ვაკეთებთ მხოლოდ ფუნქციის შიგნით და არა მთელ პროგრამაში.

#3 პარამეტრი არის ცვლადი, რომელსაც მივუთითებთ ფუნქციის შექმნისას (დეკლარირებისას) მის ფრჩხილებში. ეს არის ერთგვარი ადგილმკავებელი (placeholder), რომელიც ფუნქციას ეუბნება: როცა გამომიძახებენ, აქ რაღაც მნიშვნელობას გადმომცემენ და მე ამ სახელით გამოვიყენებ.
#4 არგუმენტი არის რეალური მნიშვნელობა, რომელსაც ფუნქციას გადავცემთ მისი გამოძახების მომენტში. ეს არის კონკრეტული მონაცემი, რომელიც ჩაჯდება პარამეტრის ადგილას.

#5 პარამეტრი არის ცვლადის სახელი ფუნქციის აღწერაში, ხოლო არგუმენტი არის რეალური მონაცემი ფუნქციის გამოძახებისას.

# 6
def repeat_word(word, count):
    for i in range(count):
        print(word)

# 7
def print_numbers(start, end):
    for i in range(start, end + 1): 
        print(i)

# 8
def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    print(f"ლუწი რიცხვების რაოდენობა: {count}")


# 9
def count_vowels(text):
    vowels = "აეიოუaeiou"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    print(f"ხმოვნების რაოდენობა: {count}")


# 10
def longest_word(words):
    if not words:
        return
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    print(f"ყველაზე გრძელი სიტყვაა: {longest}")


# 11
def filter_long_words(sentence, n):
    words = sentence.split()
    for word in words:
        if len(word) > n:
            print(word)


# 12
def name_lengths(names):
    for name in names:
        print(f"{name} - {len(name)}")


# 13
def find_max(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    print(f"მაქსიმალური რიცხვი: {max_num}")


# 14
def find_min(numbers):
    if not numbers:
        return None
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    print(f"მინიმალური რიცხვი: {min_num}")


# 15
def remove_duplicates(numbers):
    unique_list = []
    for num in numbers:
        if num not in unique_list:
            unique_list.append(num)
    print(f"სია დუბლიკატების გარეშე: {unique_list}")


# 16
def analyze_numbers(numbers):
    if not numbers:
        print("სია ცარიელია")
        return

    total_sum = 0
    for num in numbers:
        total_sum += num
        
    avg = total_sum / len(numbers)
    
    max_num = numbers[0]
    min_num = numbers[0]
    even_count = 0
    
    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
        if num % 2 == 0:
            even_count += 1
            
    print(f"ჯამი: {total_sum}")
    print(f"საშუალო არითმეტიკული: {avg}")
    print(f"ყველაზე დიდი რიცხვი: {max_num}")
    print(f"ყველაზე პატარა რიცხვი: {min_num}")
    print(f"ლუწი რიცხვების რაოდენობა: {even_count}")




print("--- მე-12 დავალების ტესტირება ---")
user_names = input("შემოიტანეთ რამდენიმე სახელი (დააშორეთ სფეისით): ")
names_list = user_names.split()
name_lengths(names_list)

print("\n--- მე-16 დავალების ტესტირება ---")
user_numbers = input("შემოიტანეთ რამდენიმე რიცხვი (დააშორეთ სფეისით): ")

numbers_list = [int(x) for x in user_numbers.split()]
analyze_numbers(numbers_list)