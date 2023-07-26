time = input('!')

def convert_hours(time):

    time = time.split(':')
    print(f' time = {time}')
    if len(time) != 2:
        print('Error: must have two numbers separated by a colon.')
        print(f'debug: {time}')
        exit(-1)

    hours = int(time[0])
    minutes = float(time[1]) / 60

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

convert_hours(time)


#problemas: se o input for palavras ou letras, não está impedido;