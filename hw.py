with open('recipes.txt', 'r', encoding='utf-8') as recipes:
    cook_book = {}

    for line in recipes:
        if '|' not in line and not line.strip().isdigit() and line.strip() != '':
            cook_book.setdefault(line.strip())
            key = line.strip()
            cook_book[key] = []

        if '|' in line:
            ingredient = line.strip().split(' | ')
            dict_ingr = {'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]}
            cook_book[key].append(dict_ingr)


for key in cook_book:
    print(key)
    print(cook_book[key])






print(cook_book.keys())