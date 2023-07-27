def get_cook_book():
    with open('recipes.txt', 'r', encoding='utf-8') as recipes:
        cook_book = {}

        for line in recipes:
            if '|' not in line and not line.strip().isdigit() and line.strip() != '':
                cook_book.setdefault(line.strip())
                key = line.strip()
                cook_book[key] = []

            if '|' in line:
                ingredient = line.strip().split(' | ')
                dict_ingr = {'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]), 'measure': ingredient[2]}
                cook_book[key].append(dict_ingr)

    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_cook_book()
    shop_list = {}
    for dish in dishes:
        for idx, ingr in enumerate(cook_book[dish]):
            if ingr['ingredient_name'] not in list(shop_list.keys()):
                shop_list[ingr['ingredient_name']] = {'measure': ingr['measure'],
                                                      'quantity': (ingr['quantity'] * person_count)}
            else:
                shop_list[ingr['ingredient_name']]['quantity'] += ingr['quantity'] * person_count

    return shop_list


print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))