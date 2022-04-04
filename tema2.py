def unidentified_function(*parameters, ):
    print(parameters)
    suma = 0
    for a in parameters:
        if type(a) == int or type(a) == float:
            suma = suma + a
    print('Suma parametrilor =', suma, '\n\n')


unidentified_function(1, 2, 3.4, 'abc', 3, 4+7j, 'Ana nu mai are mere', 5)


def recurs(n):            # 0+1+2+3+4+5+6 = 21
    if n == 0:
        return 0
    return n + recurs(n-1)


suma2 = recurs(6)
print('suma numerelor de la [0,n] =', suma2, '\n')


def recurs(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if n % 2 == 0:
        return n + recurs(n-2)
    else:
        return n + recurs(n-2)


# 0+1+2+3+4+5+6+7 = 16
suma2 = recurs(7)
print('suma numerelor de la [0,n] =', suma2, '\n\n')


a = input()


def an_function(a):
    try:
        a = int(a)
        print('numarul tau este =', a)
    except ValueError:
        print(0)


an_function(a)
