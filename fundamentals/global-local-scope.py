#Global scope
num1 = 100
num2 = 40

def add():
    #local scope
    # num1 = 20
    # num2 = 10
    addition = num1 + num2
    print(addition)

def sub():
    #local scope
    # num1 = 50
    # num2 =10
    subtraction = num1 - num2
    print(subtraction)

add()
sub()