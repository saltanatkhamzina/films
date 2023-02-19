from django.shortcuts import render, redirect
from .models import Ad, Category
from .forms import AdForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

# Create your views here.
@login_required(login_url='/login/')
def new(request):
    form = AdForm(request.POST or None)
    if request.method == "POST":
        form = AdForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user
            ad.save()
            for i in form.cleaned_data['categories']:
                category = Category.objects.get(pk=i)
                ad.categories.add(category)
            ad.save()
    form = AdForm()
    return render(request, 'new.html', {'form': form, 'title': 'Новое объявление'})


class AdsListView(ListView):
    model = Ad
    template_name = 'ads/all.html'  
    context_object_name = 'ads'
    ordering = ['-created']