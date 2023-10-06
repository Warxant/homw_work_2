# with open('1.txt', 'r', encoding='utf-8') as a, open('2.txt', 'r', encoding='utf-8') as b, open('3.txt', 'w', encoding='utf-8') as c:
#     one = a.read()
#     duo = b.read()
#     name_1 = ('1.txt')
#     name_2 = ('2.txt')
#     if len(one) > len(duo):
#         c.write(f'{name_2}\n')
#         c.write(f'{str(len(duo))}\n')
#         c.write(f'{duo}\n')
#         c.write(f'{name_1}\n')
#         c.write(f'{str(len(one))}\n')
#         c.write(one)
#     elif len(one) < len(duo):
#         c.write(f'{name_1}\n')
#         c.write(f'{str(len(one))}\n')
#         c.write(f'{one}\n')
#         c.write(f'{name_2}\n')
#         c.write(f'{str(len(duo))}\n')
#         c.write(f'{duo}\n')
#     else:
#         print('Ошибка')
#
#     a.close()
#     b.close()



with open('kslu.txt', 'r', encoding='utf-8') as f:
    cook_book = {}
    for dish in f:
        quantity_ingredient = int(f.readline())
        ingredients = []
        for ingredient in range(quantity_ingredient):
            name, quantity, measure = f.readline().strip().split('|')
            ingredients.append({
                'ingredient_name': name,
                'quantity': quantity,
                'measure': measure
            })
        f.readline()
        cook_book[dish.strip()] = ingredients

def get_shop_list_by_dishes(dishes, person_count):
    ingrediend_to_cooking = {}
    dish = []
    for i in dishes:
        dish.append(cook_book[i])
    for j in dish:
        for i in j:
            if i['ingredient_name'] not in ingrediend_to_cooking:
                ingrediend_to_cooking[i['ingredient_name']] = {'measure': (i['measure']), 'quantity': (int(i['quantity']) * person_count)}
            else:
                q = int(i['quantity']) * person_count
                ingrediend_to_cooking[i['ingredient_name']] = {'measure': (i['measure']),
                                                               'quantity': (q + int(i['quantity']) * person_count)}
    return ingrediend_to_cooking

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))








