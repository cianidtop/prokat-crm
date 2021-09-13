from django.shortcuts import render
from django.db.models import Q, Sum, Count
from datetime import date, datetime

from ride.models import Ride

def auth(request):
    return render(request, 'main/auth.html')

def main(request):
    data = {
        'sum_day': Ride.objects.filter(start_time__date=datetime.now().date()).aggregate(total_sum=Sum("cena")),
        'cash_sum_day_iskra': Ride.objects.filter(start_time__date=datetime.now().date(),
                                            payment_type__startswith='Наличный',
                                              place_from__startswith='Искра').aggregate(total_sum=Sum("cena")),
        'card_sum_day_iskra': Ride.objects.filter(start_time__date=datetime.now().date(),
                                            payment_type__startswith='Безналичный',
                                              place_from__startswith='Искра').aggregate(total_sum=Sum("cena")),
        'mixed_sum_day_iskra': Ride.objects.filter(start_time__date=datetime.now().date(),
                                            payment_type__startswith='Смешанный',
                                              place_from__startswith='Искра').aggregate(total_sum=Sum("cena")),
        'cash_sum_day_nab': Ride.objects.filter(start_time__date=datetime.now().date(),
                                                  payment_type__startswith='Наличный',
                                                place_from__startswith='Набережная').aggregate(total_sum=Sum("cena")),
        'card_sum_day_nab': Ride.objects.filter(start_time__date=datetime.now().date(),
                                                  payment_type__startswith='Безналичный',
                                                place_from__startswith='Набережная').aggregate(
            total_sum=Sum("cena")),
        'iskra_sum_day': Ride.objects.filter(start_time__date=datetime.now().date(),
                                             place_from__startswith='Искра').aggregate(
            total_sum=Sum("cena")),
        'nab_sum_day': Ride.objects.filter(start_time__date=datetime.now().date(),
                                           place_from__startswith='Набережная').aggregate(
            total_sum=Sum("cena")),
    }
    return render(request, 'main/main.html', data)

def clients(request):
    return render(request, 'main/client.html')

def tech(request):
    return render(request, 'main/tech.html')
