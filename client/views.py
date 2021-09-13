from django.shortcuts import render, redirect, get_object_or_404
from .models import Client
from .forms import ClientForm

from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.core.paginator import Paginator


class SearchResultsView(ListView):
    model = Client
    template_name = 'client/client_search.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Client.objects.filter(Q(first_name__icontains=query) | Q(phone_number__icontains=query) | Q(id__icontains=query) | Q(last_name__icontains=query))
        return object_list

def client(request):
    client_list = Client.objects.all()
    paginator = Paginator(client_list, 20)  # Show 25 contacts per page

    page = request.GET.get('page')
    client = paginator.get_page(page)
    return render(request, 'client/client.html', {'client': client})

def clientnew(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('ridenew')
    else:
        form = ClientForm()
        return render(request, 'client/clientnew.html', {'form': form})


def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save(commit=False)
            client.save()
            return redirect('client_detail', pk=client.id)
    else:
        form = ClientForm(instance=client)
    return render(request, 'client/clientnew.html', {'form': form})



def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'client/client_detail.html', {'client': client})
