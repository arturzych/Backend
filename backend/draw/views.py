from django.shortcuts import render
from random import randint
# Create your views here.


def toto(request):
    num = []
    a = len(num)
    while a < 6:
        r = randint(1, 49)
        if num.count(r) == 0:
            num.append(r)
        else:
            print(f'więcej niż 1 numer {r}')
            a = a - 1
        a = a + 1
        num.sort()
    print(num)

    return render(
        request,
        'draw/toto-lotek.html',
        context={
            'num': num,


        }
    )