ticket = 0
quant = (int(input("Введиде количество билетов:")))
for age in range(quant):
    age = (int(input("Введите возраст посеттеля:")))
    if age < 18:
        ticket += 0
    elif age >= 18 and age <= 25:
        ticket += 990
    elif age > 25:
        ticket += 1390
if ticket == 0:
    print("Дети проходят бесплатно!")
else:
    print("Сумма", ticket)
if quant > 3:
    discount = ticket / 100 * 10
    print("Скидка 10%", discount)
    print("Сумма к оплате", ticket - discount)
