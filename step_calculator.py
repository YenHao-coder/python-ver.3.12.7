# 待辦事項1: 請寫出減法函式、乘法函式、除法函式
import calculator_art
def add(n1,n2):
    sum = n1 + n2
    return sum

def subtract(n1,n2):
    diffrence = n1 - n2
    return diffrence

def multiple(n1,n2):
    product = n1 * n2
    return product

def div(n1,n2):
    quotient = n1 / n2
    return quotient

#待辦事項: 將4種函數集成為字典，以'+', '-', '*', '/'為key
operations = {
    '+':add, 
    '-':subtract, 
    '*':multiple, 
    '/':div}

#待辦事項: 用"operation"表示相乘。例: 4*8

# test = operations['*'](4,8)
# print(test)

#待辦事項1: 詢問第一個數字
#待辦事項2: 詢問運算方式: +, -, *, /
#待辦事項3: 詢問第二個數字
#待辦事項4: 將數字1與數字2的計算過程與結果列印，並詢問是否繼續計算


def calculator():
    print(calculator_art.logo)
    number1 = float(input("What's the first number? "))
    continue_calc = True

    while continue_calc:
        operator = f'{input("+\n-\n*\n/\nPick an operation: ")}'
        number2 = float(input("What's the next number? "))
        result = operations[operator](number1,number2)
        print(f"{number1} {operator} {number2} = {result}")
        
        claculating_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if claculating_continue == 'y':
            number1 = result
        else:
            continue_calc = False
            print("\n" * 20)
    
calculator()
