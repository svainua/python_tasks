# Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых (каждый год размер его вклада увеличивается на 10%. 
# Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
# Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.


def bank(deposit, years, rate):
    final_amount = deposit
    for total in range(years):
        final_amount += (final_amount * rate) / 100
    return round(final_amount, 2)



deposit = int(input("What if your deposit?:\n"))
years = int(input("For how many years?:\n"))
interest_rate = float(input("What is the interest rate?:\n"))

result = bank(deposit, years, interest_rate)

print(result)