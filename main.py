# 1
list = [1, 2, 3, 4, 5]
print(list)

# 2
def sum_of_list(l):
    total = 0
    for i in l:
        total += i
    return total
print(sum_of_list(list))

# 3
my_list = ["Gouda", "Stilton", "Gorgonzola", "Cheddar"]
print(my_list[-1])

# 4
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

# 5
fruits.remove("banana")
print(fruits)

# 1
# A function is a type of subprogram that returns an output, usually when given input parameters. It is useful to avoid repetition

# 2
def greet(name):
    print(f'Hello, {name}')

# 3
def product(a, b):
    return a * b

# 4
def is_even(n):
    return n % 2 == 0
