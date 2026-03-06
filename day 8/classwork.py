#age_input = input("შეყვანეთ თქვენი ასაკი: ") 
#age = int(age_input)
#age >= 18
#print(age_input)

beka_langs = {"Python", "C#", "HTML"}
friend_langs = {"Python", "JavaScript"}

common = beka_langs & friend_langs      # пересечение
only_beka = beka_langs - friend_langs   # только у тебя
all_langs = beka_langs | friend_langs   # объединение

print(common)    # {'Python'}
print(only_beka) # {'C#', 'HTML'}
print(all_langs) # {'Python', 'C#', 'HTML', 'JavaScript'}

