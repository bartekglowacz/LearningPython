fruits = ['apple', 'orange', 'pear', 'banana', 'apple']

print("Start")

for i, fruit in enumerate(fruits):
    print("Sprawdzam {}".format(i))
    if i == 3:
        break
    print("{} jest ok. ".format(fruit))

print("Koniec")