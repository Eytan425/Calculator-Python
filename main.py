#Calculator in Python

def Add(num1, num2):
    result = num1+num2
    return f"{num1} + {num2} = {result}"

def Sub(num1, num2):
    result = num1-num2
    return f"{num1} - {num2} = {result}"


def Div(num1,num2):
    result = num1/num2
    return f"{num1} / {num2} = {result}"


def Mutly(num1, num2):
    result = num1*num2
    return f"{num1} * {num2} = {result}"



def Calculator():
    while(True):
        operator = ['+', ',','*','/']
        start = input("Would you like to start [y/n]? ")
        if start.lower() == 'y':
            num1 = int(input("Enter a number: "))
            choice = input("Enter the operator you would like to use: ")
            num2 = int(input("Enter a number: "))
            if choice in operator:
                match choice:
                    case "+":
                        return Add(num1,num2)
                    case "-":
                        return Sub(num1,num2)
                    case "*":
                        return Mutly(num1,num2)
                    case "/":
                        return Div(num1,num2)
                    case default:
                        return "Didn't understand"
            else:
                return "Not one of the choices"
        elif start.lower() == 'n':
            return "Goodbye!"
            


print(Calculator())            
                