def ask_user(say):
    while True:
        if say == 'Хорошо':
            print('Поздравляю')
            break
        else:
            print('Хм')
            say = input('Что-нибудь')

print(ask_user(input('Anythink')))