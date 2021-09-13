from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import RideForm
from django.views.generic import TemplateView, ListView
from django.db.models import Q, Sum, Count
from datetime import date, datetime
from client.models import Client
from django.core.paginator import Paginator
from .chart import *


today_date = datetime.now().date()

class SearchResultsView(ListView):
    model = Ride
    template_name = 'ride/ride_search.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Ride.objects.filter(Q(tech__icontains=query) | Q(phone_number__icontains=query) | Q(last_name__icontains=query))
        return object_list

def ride(request):
    ride_list = Ride.objects.all()
    paginator = Paginator(ride_list, 20)  # Show 25 contacts per page

    page = request.GET.get('page')
    ride = paginator.get_page(page)
    return render(request, 'ride/ride.html', {'ride': ride,
                                              'sum_day': Ride.objects.filter(start_time__date=datetime.now().date()).aggregate(total_sum = Sum("cena"))})



def ridenew(request):
    if request.method == "POST":
        form = RideForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('ride')
    else:
        form = RideForm()
        return render(request, 'ride/ridenew.html', {'form': form})

def ride_detail(request, pk):
    ride = get_object_or_404(Ride, pk=pk)
    return render(request, 'ride/ride_detail.html', {'ride': ride})


def ride_edit(request, pk):
    ride = get_object_or_404(Ride, pk=pk)
    if request.method == "POST":
        form = RideForm(request.POST, instance=ride)
        if form.is_valid():
            ride = form.save(commit=False)
            ride.save()
            return redirect('ride_detail', pk=ride.id)
    else:
        form = RideForm(instance=ride)
    return render(request, 'ride/ridenew.html', {'form': form})

def cash(request):

    data = {'sum': Ride.objects.aggregate(total_sum = Sum("cena")),
            'tech_pie': render_pie_tech(),
            'chart': create_chart(),
            'pie': render_pie(),
            'months': render_months(),
            'cars': create_cars_chart(),
            'months_cars': render_months_cars(),
            'sum_day': Ride.objects.filter(start_time__date=datetime.now().date()).aggregate(total_sum = Sum("cena")),
            'cash_sum_day': Ride.objects.filter(start_time__date=datetime.now().date(),
                                                payment_type__startswith='Наличный').aggregate(total_sum = Sum("cena")),
            'card_sum_day': Ride.objects.filter(start_time__date=datetime.now().date(),
                                                payment_type__startswith='Безналичный').aggregate(total_sum=Sum("cena")),
            'mixed_sum_day': Ride.objects.filter(start_time__date=datetime.now().date(),
                                                payment_type__startswith='Смешанный').aggregate(total_sum=Sum("cena")),
            'iskra_sum_day': Ride.objects.filter(start_time__date=datetime.now().date(),
                                                place_from__startswith='Искра').aggregate(
                total_sum=Sum("cena")),
            'nab_sum_day': Ride.objects.filter(start_time__date=datetime.now().date(),
                                                place_from__startswith='Набережная').aggregate(
                total_sum=Sum("cena")),
            'sum_day_samokat': Ride.objects.filter(start_time__date=datetime.now().date(),
                                                   tech__startswith='Самокат').aggregate(total_sum=Sum("cena")),
            'sum_day_bike': Ride.objects.filter(start_time__date=datetime.now().date(),
                                                tech__startswith='Байк').aggregate(total_sum=Sum("cena")),
            'sum_day_velik': Ride.objects.filter(start_time__date=datetime.now().date(),
                                                 tech__startswith='Велосипед').aggregate(total_sum=Sum("cena")),
            'sum_day_car': Ride.objects.filter(start_time__date=datetime.now().date(),
                                               tech__startswith='Машинка').aggregate(total_sum=Sum("cena")),
            'cnt_day': Ride.objects.filter(start_time__date=datetime.now().date()).aggregate(total_cnt = Count("cena")),
            'cnt_day_client': Client.objects.filter(start_time__date=datetime.now().date()).aggregate(total_cnt = Count("first_name")),
            'sum_iskra': Ride.objects.filter(place_from__startswith='Искра').aggregate(total_sum = Sum("cena")),
            'sum_nab': Ride.objects.filter(place_from__startswith='Набережная').aggregate(total_sum = Sum("cena")),
            'sum_samokat': Ride.objects.filter(tech__startswith='Самокат').aggregate(total_sum=Sum("cena")),
            'sum_bike': Ride.objects.filter(tech__startswith='Байк').aggregate(total_sum=Sum("cena")),
            'sum_velik': Ride.objects.filter(tech__startswith='Велосипед').aggregate(total_sum=Sum("cena")),
            'sum_car': Ride.objects.filter(tech__startswith='Машинка').aggregate(total_sum=Sum("cena")),
            'cnt_ride': Ride.objects.aggregate(total_cnt = Count("cena")),
            'cnt_client': Client.objects.aggregate(total_cnt = Count("first_name")),
            'cnt_iskra': Ride.objects.filter(place_from__startswith='Искра').aggregate(total_cnt = Count("cena")),
            'cnt_nab': Ride.objects.filter(place_from__startswith='Набережная').aggregate(total_cnt = Count("cena")),
            'cnt_samokat': Ride.objects.filter(tech__startswith='Самокат').aggregate(total_cnt=Count("cena")),
            'cnt_bike': Ride.objects.filter(tech__startswith='Байк').aggregate(total_cnt=Count("cena")),
            'cnt_velik': Ride.objects.filter(tech__startswith='Велосипед').aggregate(total_cnt=Count("cena")),
            'cnt_car': Ride.objects.filter(tech__startswith='Машинка').aggregate(total_cnt=Count("cena")),
            }
    return render(request, 'ride/cash.html', data)
