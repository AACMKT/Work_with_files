from pprint import pprint
with open('recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dishes_name = line.strip()
        line_count = int(file.readline())
        ingredients = []
        for _ in range(line_count):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure': measure
            })
        file.readline()
        cook_book[dishes_name] = ingredients
    pprint(cook_book, sort_dicts=False, width=100)
    print('\n')


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for k, v in cook_book.items():
        if k in dishes:
            for i in v:
                i['quantity'] = i['quantity'] * person_count
                if i['ingredient_name'] not in shop_list.keys():
                    shop_list[i.pop('ingredient_name')] = i
                else:
                    shop_list[i['ingredient_name']]['quantity'] += int(i['quantity'])

    return shop_list


pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 10), sort_dicts=True)
