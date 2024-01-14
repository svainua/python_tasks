#Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.

#Если год не делится на 4, то он обычный.
#Если год делится на 4, но не делится на 100, то он високосный.
#Если год делится на 100, но не делится на 400, то он обычный.
#Если год делится и на 100, и на 400, то он високосный.


def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("It's a leap year")  
            else:
                print("Not a leap year")      
        else:
            print("It's a leap year")    
    else:
        print("Not a leap year")    

leap_year(2024)

