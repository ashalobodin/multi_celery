from celeryapp import app


@app.task
def factorial(x=3):
    x = int(x)
    res = 1
    for i in range(1, x + 1):
        res *= i
    return {'factorial of {x} is'.format(x=x): res}


@app.task
def dictionary(dct=None):
    res = list(dct.keys()) if dct else []
    return {'keys': res, 'dict': dct}


@app.task
def lst(lst=(1, 2, 3)):
    l = len(lst)
    return {'length': l, 'first': lst[0], 'rest': lst[1:]}
