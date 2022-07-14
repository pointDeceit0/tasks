import datetime

def calculate_age(born: str) -> int:

    '''
    input  ---    DD MM YYYY   ---   by space
    '''

    born = list(map(int, born.strip().split()))

    born = datetime.datetime(year=born[2], month=born[1], day=born[0])

    today = datetime.date.today()

    ''' если число дней больше сегодняшнего числа дней, то отнимаем еще год '''
    ifmore = ((today.month, today.day) < (born.month, born.day))

    return today.year - born.year - ifmore


def main():

    birth = input('input your birthday DD MM YYYY: ')

    print(calculate_age(birth))


if __name__ == "__main__":
    main()


