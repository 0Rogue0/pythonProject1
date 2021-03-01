import numpy as np


def f21(x):
    if (x[2] == 'cuda'):
        if (x[3] == 'apl'):
            return 13
        elif (x[3] == 'tea'):
            return 12
        elif (x[3] == 'xbase'):
            if (x[4] == 1988):
                return 1
            elif (x[4] == 1965):
                if (x[0] == 'text'):
                    return 10
                elif (x[0] == 'forth'):
                    return 9
    elif (x[2] == 'raml'):
        if (x[4] == 1988):
            if (x[3] == 'apl'):
                return 8
            elif (x[3] == 'tea'):
                if (x[0] == 'text'):
                    return 7
                elif (x[0] == 'forth'):
                    return 6
            elif (x[3] == 'xbase'):
                if (x[1] == 'nesc'):
                    return 5
                elif (x[1] == 'volt'):
                    return 4
        elif (x[4] == 1965):
            if (x[3] == 'apl'):
                if (x[1] == 'nesc'):
                    return 3
                elif (x[1] == 'volt'):
                    return 2
            elif (x[3] == 'tea'):
                return 1
            elif (x[3] == 'xbase'):
                return 0


def f22(x):
    a = x & 0b11
    x >>= 2
    a <<= 0

    b = x & 0b1
    x >>= 1
    b <<= 2

    c = x & 0b11111111111
    x >>= 11
    c <<= 20

    d = x & 0b11111111111111
    x >>= 14
    d <<= 3

    e = x & 0b11
    x >>= 2
    e <<= 18

    return c | e | d | b | a


def f23(x):
    stfinal = []
    skip = 0  # пустая строка
    colums = 0
    for i in range(0, len(x)):  # цикл ищет пустые столбцы
        for j in range(0, len(x)):
            for nspisok in x[i][j]:
                if nspisok is None:
                    colums += 1
                    break
    for i in range(0, len(x)):
        ncounter = 0
        for j in range(0, colums):  # удаление пустых столбцов
            if nspisok is None:
                del x[i][j]
                ncounter = 1
                break
            if ncounter == 1:
                break
    for i in range(0, len(x)):  # в цикл поступает информация о количестве пустык строк в таблице
        for spisok in x[i]:
            if spisok is None:
                skip += 1
                break
    for i in range(0, skip):
        counter = 0
        for j in range(0, len(x)):  # цикл начинает отсчёт пустых строк, начиная с 0, а затем удаляет их
            if spisok is None:
                del x[j]
                counter = 1
                break
            if counter == 1:
                break

    for i in x:  # удаление повторений
        if i not in stfinal:
            stfinal.append(i)

    for i in range(0, len(x)):
        date = x[i][0].find('&')
        x[i][2] = x[i][0][date + 1:]
        email = x[i][1].find('[at]')
        x[i][1] = x[i][1][email + 4:]
        byfer = x[i][1]
        ready = ""
        for k in range(0, byfer):
            if byfer[k] != "at":
                ready += byfer[k]
            else:
                x[i][1] = ready + email
                ready = ""
                break
        x[i][2] = x[i][2][6:9] + x[i][2][2] + x[i][2][3:4] + x[i][2][5] + x[i][2][0:1]
        round(x[i][1])
    return stfinal


print(f23([[None, None, None, None], ["0.786 & 15 / 0o7 / 2003", "dofidi39[at]mail.ru", None, "dofidi39[at]mail.ru"],
           ["0.295&22/09/2000", "kocj55[at]mail.ru", None, "kocj55[at]mail.ru"],
           ["0.940&16/05/2003", "mitilskij32[at]rambler.ru", None, "mitilskij32[at]rambler.ru"]]))
print(f23([["0.486&06/06/1999", "kirill47[at]rambler.ru", None, "kirill47[at]rambler.ru"],
           ["0.417&14/12/1999", "gebodanz93[at]gmail.com", None, "gebodanz93[at]gmail.com"],
           [None, None, None, None],
           ["0.635&14/07/2001", "messkiji28[at]gmail.com", None, "messkiji28[at]gmail.com"]]))
