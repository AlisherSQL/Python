Create custom modules.
Create math_operations.py module. Define add, subtract, multiply and divide functions in it. (All functions accept two arguments in this task)
Create string_utils.py module. Define reverse_string and count_vowels functions in it. (All functions accept one argument in this task)

func.py
def add(a,b):
    return a+b

def multply(a,b):
    return a*b

greet.py

def Say(name):
    return name[::-1]

def count (s):
    vouv='aeiou'
    return sum(1 for char in s if char in vouv)    

from MyPakeg import func as w
print(w.add(22,4))

from MyPakeg import greet
print (greet.Say('asdd'))
