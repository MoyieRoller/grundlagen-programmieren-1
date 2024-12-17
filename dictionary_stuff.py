fruit_prices = {
    'apple': 1.0,
    'banana': 0.5,
    'orange': 0.75,
}

# print apple price
print(fruit_prices['apple'])
print(fruit_prices.get('applle', 0))

# add kiwi price
fruit_prices['kiwi'] = 0.2
# fruit_prices.update({'kiwi': 0.2})

# print item count
print('Total amount of fruit in dic', len(fruit_prices))

# change banana price
fruit_prices.update({'banana': 0.6})
print('New banana price:', fruit_prices['banana'])

# delete orange
fruit_prices.pop('orange')

# check if apple and cherry exist in dictionary
print('apple' in fruit_prices)
print('cherry' in fruit_prices)

# total price
def get_total_price(fruit_list):
    total_price = 0

    for fruit in fruit_list:
        if fruit in fruit_prices:
            total_price += fruit_prices[fruit]
        else:
            print(f'Attention, {fruit} not in price list.')
    return total_price

print('Total fruit price:', get_total_price(['apple', 'banana', 'kiwi']))
print('Total fruit price:', get_total_price(['apple', 'banana', 'mango']))

# lowest price
def get_cheapest_fruit(dict):
    fruit = list(dict.values())
    fruit.sort()
    return fruit[0]

print('Lowest price:', get_cheapest_fruit(fruit_prices))

min_val = 10000
min_fruit = ''

for fruit, price in fruit_prices.items():
    if price < min_val:
        min_val = price
        min_fruit = fruit

print(min_fruit, min_val)