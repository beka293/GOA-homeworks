# min(): ეს ფუნქცია არგუმენტად იღებს კოლექციას (მაგალითად, სიას) ან რამდენიმე მნიშვნელობას და აბრუნებს მათ შორის ყველაზე მცირეს.

# max(): min()-ის საპირისპიროა. ის ეძებს და აბრუნებს გადაცემულ მნიშვნელობებს შორის ყველაზე დიდს.

# sum(): ეს ფუნქცია აჯამებს სიის (ან სხვა იტერირებადი ობიექტის) შიგნით არსებულ ყველა რიცხვით მნიშვნელობას და აბრუნებს მათ საერთო ჯამს.

# ონლაინ მაღაზიაში: min() და max() ფუნქციებით შეგვიძლია მომხმარებელს ვუჩვენოთ ყველაზე იაფი და ყველაზე ძვირი პროდუქტი, ხოლო sum()-ით დავუთვალოთ კალათაში არსებული ნივთების საერთო ღირებულება.

def max_difference(numbers):
    if not numbers:
        return 0
    return max(numbers) - min(numbers)


def unique_characters(text):
    result = []
    for char in text:
        if text.count(char) == 1 and char not in result:
            result.append(char)
    return result


def highest_char(text):
    if not text:
        return ""
    return max(text)


def numbers_summary(numbers):
    if not numbers:
        return ""
    return f"რაოდენობა: {len(numbers)} | ჯამი: {sum(numbers)} | მინიმალური: {min(numbers)} | მაქსიმალური: {max(numbers)}"


def char_code_sum(text):
    total_sum = 0
    for char in text:
        total_sum += ord(char)
    return total_sum


print(max_difference([8, 3, 15, 6]))
print(unique_characters("banana"))
print(highest_char("Az9"))
print(numbers_summary([5, 10, 15]))
print(char_code_sum("ABC"))