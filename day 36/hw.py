# 1)
# return ბრძანება ფუნქციაში გამოიყენება იმისთვის, რომ ფუნქციამ მისი მუშაობის დასრულების შემდეგ უკან, პროგრამას, დაუბრუნოს კონკრეტული შედეგი (მნიშვნელობა). როდესაც კოდი მიაღწევს return-ს, ფუნქციის შესრულება წყდ






# 2) 
def greet():
    return "Hello, World!"

# 3)
def square(number):
    return number ** 2

# 4) 
def add(a, b):
    return a + b

# 5)
def is_even(number):
    return number % 2 == 0

# 6)
def count_vowels(text):
    vowels = "aeiouAEIOUაეიოუ"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# 7) 
def largest(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# 8) 
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# 9) 
def count_letter(text, letter):
    count = 0
    for char in text:
        if char == letter:
            count += 1
    return count

# 10) 
def filter_even(numbers):
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

# 11) 
def format_name(name):
    return name.title()

# 13) 
def remove_duplicates(numbers):
    unique_list = []
    for num in numbers:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list

# 14)
def second_largest(numbers):
    if len(numbers) < 2:
        return None
    unique_sorted = sorted(list(set(numbers)))
    return unique_sorted[-2]

# 18)
def count_occurrences(numbers, target):
    count = 0
    for num in numbers:
        if num == target:
            count += 1
    return count

# 19) 
def merge_lists(list1, list2):
    merged = []
    for item in list1:
        merged.append(item)
    for item in list2:
        merged.append(item)
    return merged

# 20) 
def analyze_numbers(numbers):
    if not numbers:
        return []
    max_num = max(numbers)
    min_num = min(numbers)
    total_sum = sum(numbers)
    count = len(numbers)
    average = total_sum / count
    return [max_num, min_num, total_sum, count, average]



print("--- დავალება 2 ---")
print(greet())

print("\n--- დავალება 3 ---")
print(square(4))
print(square(9))

print("\n--- დავალება 4 ---")

num1 = float(input("შემოიტანეთ პირველი რიცხვი: "))
num2 = float(input("შემოიტანეთ მეორე რიცხვი: "))
print("ჯამი:", add(num1, num2))

print("\n--- დავალება 5 ---")
print(is_even(4))
print(is_even(7))

print("\n--- დავალება 6 ---")
print(count_vowels("Python პროგრამირება"))

print("\n--- დავალება 7 ---")
print(largest([3, 5, 9, 2, 8]))

print("\n--- დავალება 8 ---")
print(sum_list([10, 20, 30]))

print("\n--- დავალება 9 ---")
print(count_letter("hello helsinki", "h"))

print("\n--- დავალება 10 ---")
print(filter_even([1, 2, 3, 4, 5, 6]))

print("\n--- დავალება 11 ---")
user_name = input("შემოიტანეთ თქვენი სახელი: ")
print(format_name(user_name))

print("\n--- დავალება 13 ---")
print(remove_duplicates([1, 2, 2, 3, 1, 4]))

print("\n--- დავალება 14 ---")
print(second_largest([4, 7, 2, 9, 5]))

print("\n--- დავალება 18 ---")
print(count_occurrences([1, 2, 3, 2, 4, 2], 2))

print("\n--- დავალება 19 ---")
print(merge_lists([1, 2], [3, 4]))

print("\n--- დავალება 20 ---")
print(analyze_numbers([4, 8, 2, 6]))