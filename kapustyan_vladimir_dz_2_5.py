item_prices = [57.8, 46.51, 10, 24.04, 60.12, 40, 77.7, 100, 1, 0.5]

message = ""  # задание A)
i = 0
while i < len(item_prices):
    price = str(item_prices[i])
    if type(item_prices[i]) == int:  # если после запятой нет цифр
        message += f'{price} рублей 00 копеек '
    elif len(price[price.index(".") + 1:]) == 1:  # если после запятой одна цифра
        message += f'{price[:price.index(".")]} рублей {price[price.index(".") + 1:] + "0"} копеек '
    elif len(price[price.index(".") + 1:]) == 2:  # если после запятой две цифры
        message += f'{price[:price.index(".")]} рублей {price[price.index(".") + 1:]} копеек '
    i += 1
print(message)

print(id(item_prices))  # задание B) доказываем, что объект не изменился после сортировки
item_prices.sort()
print(item_prices)
print(id(item_prices))  # задание B) доказываем, что объект не изменился после сортировки

new_sorted_list = sorted(item_prices, reverse=True)  # задание C)
print(new_sorted_list)

top_prices_message = ""  # задание D)
for n in range(5):
    print(f'Цена: {new_sorted_list[n]} топ {n + 1} место; ')
