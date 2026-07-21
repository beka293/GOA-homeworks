# 1) https://www.codewars.com/kata/59cfc000aeb2844d16000075
def capitalize(s):
    s1 = ''.join(c.upper() if i % 2 == 0 else c for i, c in enumerate(s))
    s2 = s1.swapcase()
    return [s1, s2]
# 2) https://www.codewars.com/kata/5aff237c578a14752d0035ae
import math

def predict_age(*ages):
    return int(math.sqrt(sum(age ** 2 for age in ages)) / 2)
# 3) https://www.codewars.com/kata/5a431c0de1ce0ec33a00000c
def even_numbers(arr, n):
    return [x for x in arr if x % 2 == 0][-n:]
# 4) https://www.codewars.com/kata/59a96d71dbe3b06c0200009c
def generate_shape(n):
    return '\n'.join('+' * n for _ in range(n))
# 5) https://www.codewars.com/kata/52aeb2f3ad0e952f560005d3
def sort_gift_code(code):
    return "".join(sorted(code))
# 6) https://www.codewars.com/kata/5b39e3772ae7545f650000fc
def remove_duplicate_words(s):
    return " ".join(dict.fromkeys(s.split()))
# 7) https://www.codewars.com/kata/59706036f6e5d1e22d000016
def words_to_marks(s):
    return sum(ord(char) - 96 for char in s)
# 8) https://www.codewars.com/kata/5680781b6b7c2be860000036
def vowel_indices(word):
    vowels = "aeiouyAEIOUY"
    return [i + 1 for i, char in enumerate(word) if char in vowels]
# 9) https://www.codewars.com/kata/556196a6091a7e7f58000018
def largest_pair_sum(numbers):
    return sum(sorted(numbers)[-2:])
# 10) https://www.codewars.com/kata/580755730b5a77650500010c 
def sort_my_string(s):
    return f"{s[::2]} {s[1::2]}"