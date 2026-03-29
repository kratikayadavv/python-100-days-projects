import art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations ={'+':add,
             '-':subtract,
             '*':multiply,
             '/':divide}
def calculator():
    print(art.logo)

    num1=float(input("enter the first number: "))
    should_accumulate = True
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        op=input("pick the operator: ")
        num2=float(input("enter the second number: "))
        answer= operations[op](num1,num2)
        print(f"{num1}{op}{num2}= {answer} ")

        choice = input(f"type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation")

        if choice.lower() == 'y':
            num1=answer
        else:
            should_accumulate =False
            print("\n"*20) #to clear cd
            calculator()
calculator()
