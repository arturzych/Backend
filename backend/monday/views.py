from django.shortcuts import render
from datetime import datetime


# Create your views here.
def isitmonday(request):
    # Metoda isoweekday zwraca nr dnia w kolejności (1-7) - pon. - niedz.
    # Metoda weekday zwraca nr dnia w kolejności (0-6) - pon. - niedz.
    day = datetime.now().isoweekday()
    is_it_monday = False
    if day == 1:
        is_it_monday = True

    return render(
        request,
        'monday/isitmonday.html',
        context={
            'is_it_monday': is_it_monday,
        }
    )