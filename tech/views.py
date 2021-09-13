from django.shortcuts import render, redirect, get_object_or_404
from .models import Tech
from .forms import TechForm
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.core.paginator import Paginator

def tech(request):
    tech_list = Tech.objects.all()
    paginator = Paginator(tech_list, 20)  # Show 25 contacts per page

    page = request.GET.get('page')
    tech = paginator.get_page(page)
    return render(request, 'tech/tech.html', {'tech': tech})


class SearchResultsView(ListView):
    model = Tech
    template_name = 'tech/tech.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Tech.objects.filter(Q(tech__icontains=query) | Q(reason__icontains=query))
        return object_list



def technew(request):
    if request.method == "POST":
        form = TechForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('tech')
    else:
        form = TechForm()
        return render(request, 'tech/technew.html', {'form': form})


def tech_edit(request, pk):
    tech = get_object_or_404(Tech, pk=pk)
    if request.method == "POST":
        form = TechForm(request.POST, instance=tech)
        if form.is_valid():
            tech = form.save(commit=False)
            tech.save()
            return redirect('tech_detail', pk=tech.id)
    else:
        form = TechForm(instance=tech)
    return render(request, 'tech/technew.html', {'form': form})



def tech_detail(request, pk):
    tech = get_object_or_404(Tech, pk=pk)
    return render(request, 'tech/tech_detail.html', {'tech': tech})