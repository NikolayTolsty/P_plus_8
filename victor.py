persons=['В.И.Ленин','Том Круз','Петр I','Жак-Ив Кусто','И.А.Бунин','Холли Берри']
bornyears=['1870','1962','1672','1910','1870','1966']
total_quests=len(persons)
while True:
    answers=[]
    corrects=0
    incorrects=0
    for person in persons:
        answer=input(f'В каком году родился(лась) {person}?> ')
        answers.append(answer)
    for n in range(total_quests):
        if bornyears[n]==answers[n]:
            corrects+=1
        else:
            incorrects+=1
    print(f'Вы дали {corrects} ({round(corrects/total_quests*100)}%) правильных ответов \
и {incorrects} ({round(incorrects/total_quests*100)}%) неправильных')
    while True:
        repeat=input('Хотите повторить игру с начала (да/нет)?> ')
        if repeat=='да' or repeat=='нет':
            break
        else: print('Ведите "да" или "нет"')
    if repeat=='нет': break