nums = [1,2,3,4,5]
myList = ["python","satanic ritual"]
fruits = ["python","satanic ritual","banana"]
def add(numbers):
    ans=0
    for item in numbers:
        ans=ans+item
    return ans
x=myList[(-1)]
fruits.append("orange")
fruits.remove("banana")
#the thing to delete based on name, how to go backward on array need to be figured out
print(fruits)
print(myList)

#a function in python isa subroutine that returns something, shortens repeated code.
name=input("what is name")
print("Hello ", name)
def product(num1,num2):
    num3=num1*num2
    return num3
# you return a value like this:
product=product(3,4)
def evenorodd(number):
    if float(number)/2 == int(float(number)/2):
        answer=True
    else:
        answer=False
    return answer
num4=int(input("number:"))
print(evenorodd(num4))
