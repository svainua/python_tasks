# Написать функцию arithmetic, принимающую 3 аргумента: 
#первые 2 - числа, третий - операция, которая должна быть произведена над ними. 
#Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе). 
#В остальных случаях вернуть строку "Неизвестная операция".

def arithmetic(num1, num2, operation):
    
    def result(res):
        print(f"{num1} {operation} {num2} = {res}")

    if operation == "+":
        result(num1 + num2)
    elif operation == "-":
        result(num1 - num2)
    elif operation == "*":
        result(num1 * num2)
    elif operation == "/":
        if num2 != 0:
            result(num1 / num2)
        else:
            print("Can not devide for 0")
    else:
        print("Wrong operation")      

a = int(input("Choose the first number:\n"))      
b = int(input("Choose the second number:\n"))
operation = input("What would you like to do with these figures?:\n")        

arithmetic(a, b, operation)



    