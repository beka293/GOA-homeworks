numbers_list = [122, 2.5, 67, 0.3, -3, 22.4, 89, 69]

def find_min_max_sum(nums):
    min_val = min(nums)
    max_val = max(nums)
 
    print(f"მინ რიცხვია: {min_val}")
    print(f"მაქს რიცხვია: {max_val}")
    
    return min_val + max_val

total_sum = find_min_max_sum(numbers_list)

print(f"ჯამი: {total_sum}")