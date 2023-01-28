import random


card_number = "".join([str(random.randint(0, 9)) for i in range(0, 16, 1)])
print(card_number)

last_four = card_number[-4::] # cztery ostatnie znaki karty
first_twelve = "".join("*" for i in range(0, 12))
# print(first_twelve)
# print(last_four)
secured_card = first_twelve + last_four
#print(secured_card)

secured_card_splitted = list(secured_card)
# print(secured_card_splitted)

for x in range(4, 16, 5):
    secured_card_splitted.insert(x, " ")
print("".join(secured_card_splitted))
