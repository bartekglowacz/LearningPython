# Create A Calculator Function Write a function in Python that accepts three parameters. Make sure the first
# parameter is an integer and the second follows mathematical operators such as +, -, /, or. And the third parameter
# will also be an integer. The function must perform the calculation and return the results. For instance,
# if the function passed 6 and 4 it must return 24.

def calculator(var1, operator, var2):
    if operator == "+":
        return var1 + var2
    if operator == "-":
        return var1-var2
    if operator == "*":
        return var1*var2
    if operator == "/":
        return var1/var2


print("Number 1: ")
var1 = int(input())
print("Number 2: ")
var2 = int(input())
print("Operator: ")
operator = input()

result = calculator(var1, operator, var2)
print(result)
