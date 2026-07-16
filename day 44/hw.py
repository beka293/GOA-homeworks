# 1) https://www.codewars.com/kata/57a083a57cb1f31db7000028
def powers_of_two(n):
    return [2**i for i in range(n + 1)]
# 2) https://www.codewars.com/kata/51c8991dee245d7ddf00000e
def reverse_words(s):
    return " ".join(s.split()[::-1])
# 3) https://www.codewars.com/kata/568dcc3c7f12767a62000038
def set_alarm(employed, vacation):
    return employed and not vacation
# 4) https://www.codewars.com/kata/577bd026df78c19bca0002c0
def correct(s):
    return s.translate(str.maketrans("501", "SOI"))
# 5) https://www.codewars.com/kata/5ad0d8356165e63c140014d4
def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0
# 6) https://www.codewars.com/kata/59342039eb450e39970000a6
def odd_count(n):
    return n // 2
# 7) https://www.codewars.com/kata/58ca658cc0d6401f2700045f
def find_multiples(integer, limit):
    return list(range(integer, limit + 1, integer))
# 8) https://www.codewars.com/kata/50654ddff44f800200000007
def solution(a, b):
    
    if len(a) < len(b):
        return a + b + a
    else:
        return b + a + b
# 9) https://www.codewars.com/kata/57a1fd2ce298a731b20006a4
def is_palindrome(s):
    
    s_lower = s.lower()
    return s_lower == s_lower[::-1]
# 10) https://www.codewars.com/kata/57f6ad55cca6e045d2000627
def square_or_square_root(arr):
    result = []
    for x in arr:
        root = x ** 0.5
        if root.is_integer():
            result.append(int(root))
        else:
            result.append(x ** 2)
    return result