time = input('!')

def convert_hours(time):
    time = time.split(':')
    print(time)

    hours = int(time[0])
    minutes = float(time[1]) / 60

    if 0 < hours < 24:
        print('good job')
    else:
        print('Value not supported. Must be between 0 and 24.')
        exit(-1)


    s = hours + minutes
    print(s)
    return s


convert_hours(time)