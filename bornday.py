bornyear=int(input('Год рождения А.С.Пушкина?'))
if bornyear==1799:
    bornday=input('День рождения А.С.Пушкина?')
    if bornday=='6 июня':
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год рождения')
