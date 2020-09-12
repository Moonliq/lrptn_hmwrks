def ask_user(say):
    expls = {'Как дела?': 'Хорошо', 'Что делаешь?': 'Программирую'}
    while True:
        if say == 'Хорошо':
            print('Поздравляю')
            break
        elif say in expls:
            print(expls[say])
            say = input('Что-нибудь')
        else:
            print('Хм')
            say = input('Что-нибудь')

print(ask_user(input('Anythink')))