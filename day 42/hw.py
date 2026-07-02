# tuple (კორტეჟი) არის მონაცემთა ტიპი Python-ში, რომელიც ინახავს ელემენტების თანმიმდევრობას. იგი ძალიან ჰგავს list-ს (სიას), თუმცა მათ შორის არის სამი პრინციპული განსხვავება:ცვალებადობა,სინტაქსი,სისწრაფე და მეხსიერება
# tuple-ს ვიყენებთ მაშინ, როდესაც მონაცემები მუდმივია და გვინდა ვიყოთ დაზღვეულები, რომ პროგრამის მუშაობისას კოდი მათ შემთხვევით ვერ შეცვლის.



def first_and_last(items):
    if len(items) == 0:
        return ()
    elif len(items) == 1:
        return (items[0],)
    return (items[0], items[-1])


def middle_element(items):
    mid_index = len(items) // 2
    return items[mid_index]


def count_occurrences(items, value):
    counter = 0
    for item in items:
        if item == value:
            counter += 1
    return counter


def contains_duplicates(items):
    return len(set(items)) != len(items)


def swap_edges(items):
    if len(items) < 2:
        return items
    return (items[-1],) + items[1:-1] + (items[0],)


def first_position(items, value):
    if value in items:
        return items.index(value)
    return -1


def tuple_summary(numbers):
    if not numbers:
        return "კორტეჟი ცარიელია"
    
    count = len(numbers)
    total_sum = sum(numbers)
    first = numbers[0]
    last = numbers[-1]
    
    return f"რაოდენობა: {count}  ჯამი: {total_sum}  პირველი: {first}  ბოლო: {last}"


def reverse_tuple(items):
    return items[::-1]