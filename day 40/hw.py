# 1) https://www.codewars.com/kata/5715eaedb436cf5606000381
def positive_sum(arr):
    total = 0
    for num in arr:
        if num > 0:
            total += num
    return total
# 2) https://www.codewars.com/kata/57a0e5c372292dd76d000d7e
def repeat_str(repeat, string):
    return string * repeat
# 3) https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0
def remove_char(s):
    return s[1:-1]
# 4) https://www.codewars.com/kata/515e271a311df0350d00000f
def square_sum(numbers):
    return sum(x**2 for x in numbers)
# 5) https://www.codewars.com/kata/55a2d7ebe362935a210000b2
def find_smallest_int(arr):
    return min(arr)
# 6) https://www.codewars.com/kata/55d24f55d7dd296eb9000030
def summation(num):
    return num * (num + 1) // 2
# 7) https://www.codewars.com/kata/54edbc7200b811e956000556
def count_sheeps(sheep):
    if not sheep: 
        return 0
    return sum(1 for s in sheep if s)
# 8) https://www.codewars.com/kata/57eae20f5500ad98e50002c5
def no_space(x):
    return x.replace(" ", "")
# 9) https://www.codewars.com/kata/582cb0224e56e068d800003c
def litres(time):
    return int(time * 0.5)
# 10) https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097
def century(year):
    return (year + 99) // 100


    