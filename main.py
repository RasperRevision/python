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
