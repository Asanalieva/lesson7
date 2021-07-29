#age = int(input())
import random
def int_input():
    num = int(input())
    return num

age2 = int_input()
print(age2)

def random_number():
    start = int(input())
    end = int(input())
    number = random.randint(start, end)
    return number

number1 = random_number()
number2 = random_number()
print(number1)
print(number2)
