def ask_date(question, date):
    answer = input(question)
    while answer != date:
        print("Не верно")
        answer = input(question)

ask_date('Введите год рождения А.С.Пушкина:', '1799')
ask_date('Ввведите день рождения Пушкин:', '6')
print('Верно')
