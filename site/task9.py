import datetime


def main(table: list[list[str]]):
    list_of_none = [None] * 6
    res = list(filter(lambda item: item != list_of_none, table))
    res = list(dict.fromkeys(tuple(i) for i in res))
    res = list(list(filter(lambda i: i is not None, j)) for j in res)
    res = list(zip(*res))
    res[0] = list("{:.3f}".format(float(record)) for record in res[0])
    res[1] = list(datetime.date.fromisoformat(
        d).strftime("%d/%m/%y") for d in res[1])
    res[2] = list(s.replace("[at]", "@") for s in res[2])
    res[3] = list(s[3:] for s in res[3])
    res[3] = list(s[::-1].replace('-', '', 1)[::-1] for s in res[3])
    return res


# a = [['0.52', None, None, '2001-01-26', 'anatolij47[at]yandex.ru', '+7 (489) 474-90-51'],
#      ['0.26', None, None, '2000-11-12', 'radmir33[at]gmail.com', '+7 (656) 651-88-13'],
#      [None, None, None, None, None, None],
#      [None, None, None, None, None, None],
#      ['0.26', None, None, '2000-11-12', 'radmir33[at]gmail.com', '+7 (656) 651-88-13'],
#      ['0.18', None, None, '2001-08-25', 'fosadij52[at]gmail.com', '+7 (984) 321-98-84']]

a = [['0.87', None, None, '2001-08-05', 'artur84[at]yahoo.com', '+7 (701) 315-82-38'],
     ['0.55', None, None, '2001-02-09', 'lobak71[at]yahoo.com', '+7 (085) 662-16-26'],
     [None, None, None, None, None, None],
     ['0.55', None, None, '2001-02-09', 'lobak71[at]yahoo.com', '+7 (085) 662-16-26'],
     [None, None, None, None, None, None],
     ['1.00', None, None, '2000-07-19', 'arsenij59[at]gmail.com', '+7 (019) 467-25-84'],
     ['0.18', None, None, '2003-01-06', 'keleridi88[at]yahoo.com', '+7 (407) 668-84-67']]


print(*main(a), sep='\n')
