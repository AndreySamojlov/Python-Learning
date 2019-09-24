def distribution_hat (age, iq = None):
    #army = False
    if age <= 3:
        return ("Вам не следовало покидать манеж.")
    elif 3 < age <= 7:
        return  ("Ваше место в детском саду.")
    elif 7 < age <= 17:
        return  ("Ваше место в школе.")
    elif 17 < age <= 21:
        if iq >= 100:
            return  ("Вы можете учиться в вузе.")
        else:
            return ("О-о-о, теперь ты в армии")
    elif age > 21 and iq >= 100:
        return ("Не служил - не мужик. Иди в программисты.")
    elif age > 21 and iq <= 100:
        return ("Вы можете идти дорогой приключений. Берегите колени.") 
    else:
        ("Вы чрезвычайно подозрительны. Мы за вами присмотрим.")   
while True:
    client_age = int(input("Введите ваш возраст: "))
    if client_age > 17:
        client_iq = int(input("Введите ваш IQ: "))
    advice = distribution_hat(client_age, client_iq)
    print(advice)