"""
Hide the Number of Credit Card
Create a function in Python that accepts credit card numbers.
Make sure that it returns a string with an asterisk except for the last four where all the characters are hidden.
For instance, if the function gets sent “5555555555555555”, then it should return “5555”.
"""

import random

card_number = []
card_number1 = []
card_number2 = []
card_number3 = []
card_number4 = []
card_number_str = "                   "

for part in range(1, 5, 1):
    card_number1.append(random.randint(0, 9))
    card_number2.append(random.randint(0, 9))
    card_number3.append(random.randint(0, 9))
    card_number4.append(random.randint(0, 9))

# print(card_number1)
# print(card_number2)
# print(card_number3)
# print(card_number4)

card_number = card_number1 + [" "] + card_number2 + [" "] + card_number3 + [" "] + card_number4
card_number = [str(x) for x in card_number]
# print(f"Numer karty: {card_number}")

card_number_str = "".join(card_number)
print(card_number_str)

# print("Naciśnij:\n1 - żeby zamazać pierwsze 12 numerów karty\n0 - żeby wyświetlić postać oryginalną")
# choice = str(input())

for x in range(0, len(card_number), 1):
    if x <= len(card_number) - 5:
        if card_number[x].isspace():
            card_number[x] == " "
        else:
            card_number[x] = "*"
    else:
        card_number[x]
    #print(card_number[x], end="")

card_number_str = "".join(card_number)
print(card_number_str)