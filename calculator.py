# Create A Calculator Function Write a function in Python that accepts three parameters. Make sure the first
# parameter is an integer and the second follows mathematical operators such as +, -, /, or. And the third parameter
# will also be an integer. The function must perform the calculation and return the results. For instance,
# if the function passed 6 and 4 it must return 24.

def calculator(var1, operator, var2):
    if operator == "+":
        return var1 + var2
    if operator == "-":
        return var1 - var2
    if operator == "*":
        return var1 * var2
    if operator == "/":
        return var1 / var2


print("Wprowadź równanie")
equation = input()

if equation.find("+") > 0:
    variables = equation.split("+")
    operator = "+"
if equation.find("-") > 0:
    variables = equation.split("-")
    operator = "-"
if equation.find("*") > 0:
    variables = equation.split("*")
    operator = "*"
if equation.find("/") > 0:
    variables = equation.split("/")
    operator = "/"

# print(f"Variables: {variables}")
var1 = int(variables[0])
var2 = int(variables[1])
# print(f"var1 = {var1}, var2 = {var2}, operator: {operator}")

print(f"Wynik: {calculator(var1, operator, var2)}")
