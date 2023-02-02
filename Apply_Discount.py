"""
Apply Discount
In python, create a function that accepts two parameters.
The first one must be the full price of an item as an integer and the second one must be the discount percentage as an integer.
The function must return the price of an item after the discount has been applied.
For an instance, if the price is 100 and the discount consists of 20, the function must return 80.
"""

print("Podaj cenę produktu")
full_price = input()
full_price = full_price.replace(",", ".")
full_price = float(full_price)

print("ile procent zniżki?")
discount_percentage = input()
discount_percentage = discount_percentage.partition("%")
discount_percentage = int(discount_percentage[0])/100
# print(discount_percentage)


def discount(full_price, discount_percentage):
    discount_price = full_price - full_price * discount_percentage
    return discount_price


discount_price = discount(full_price, discount_percentage)
print(f"Cena oryginalna {full_price} zł po obniżce {discount_percentage*100}% wynosi {discount_price}")
