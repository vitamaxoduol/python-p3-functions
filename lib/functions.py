#!/usr/bin/env python3


def greet_programmer():
    print("Hello, programmer!")



def greet(name = "Naureen"):
    print(f"Hello, {name}!")
    pass

def greet_with_default():
    print(f"Hello, programmer!")
    pass

def greet_with_default(name="Sunny"):
    print(f"Hello, {name}!")
    pass


def add(num1, num2):
    return num1 + num2
sum_of_nums = add(1, 2)
print(sum_of_nums)

def halve(number):
    if not isinstance(number, (int, float)):
        return None
    
    return number/2

result_of_halve = halve(4)
print(result_of_halve)
pass
