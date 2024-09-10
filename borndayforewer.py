while True:
    bornyear=int(input('Год рождения А.С.Пушкина?'))
    if bornyear==1799:
        while True:
            bornday=input('День рождения А.С.Пушкина?')
            if bornday=='6 июня':
                print('Верно')
                break
            else:
                print('Неверный день рождения')
        break
    else:
        print('Неверный год рождения')
