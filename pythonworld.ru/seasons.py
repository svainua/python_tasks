# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, 
#которому этот месяц принадлежит (зима, весна, лето или осень).

def season():
    month_num = int(input("Please eneter the number of the month:\n"))
    if month_num <=12:
        if month_num in range(3,6):
            print("spring")
        elif month_num in range(6,9):
            print("summer")
        elif month_num in range(9,12):
            print("autumn")     
        else:
            print("winter")        
    else:
        print("Use numbers between 1 and 12") 
        season()   


season()
