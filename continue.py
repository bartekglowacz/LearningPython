fruits = ['apple', 'orange', 'pear', 'banana', 'apple']

print("Start")

for fruit in fruits:
    if fruit == 'orange': continue
    if fruit == 'banana': break
    print(fruit)
print("Koniec")