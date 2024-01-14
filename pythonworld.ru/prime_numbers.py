# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое, и False - иначе.


def is_prime(number):
    result = True
    if number >= 2:
        for i in range(2, number - 1):
            if number % i == 0:
                result = False
    else:
        print("Use another number") 

    return result        
        
number = int(input("What the number should we check for Prime Number?:\n"))
result = is_prime(number)
print(result)


