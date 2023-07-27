def main():

    time = input('!')

    if 7 <= time <= 8:
        print('Breakfast time')
    elif 12 < time <= 13:
        print('Lunch')
    elif 18 <= time <= 19:
        print('Dinner')
    else:
        exit(-1)


def convert_hours(time):

    time = time.split(':') #único símbolo que separa os números e cria a lista. Inutiliza a utilização de outros símbolos.
    print(f'time = {time}')

    if len(time) != 2:
        print('Error: must have two numbers separated by a colon. Example: 12:34.')
        print(f'debug: {time}')
        exit(-1)

    hours = int(time[0])
    minutes = (float(time[1]) / 60)

    if not 0 <= hours <= 24:
        print('Value not supported. Hours must be between 0 and 24.')
        print(f'debug: hours = {hours}')

    if not 0 <= minutes <= 1:
        print('Value not supported. Minutes must be between 0 and 1')
        print(f'debug: minutes = {minutes}')
        exit(-1)

    s = hours + minutes
    print(s)
    return s

main()


#problemas: se o input for palavras ou letras, gera erro por causa do int e do float, mas não é apanhado antes; quebra o código;