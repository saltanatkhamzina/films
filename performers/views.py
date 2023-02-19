from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import Profile
from django.views.generic import ListView

# Create your views here.
@login_required
def all(request):
    return render(request, 'performers/all.html', {'profiles': Profile.objects.filter(role='performer').values(), 'title': 'Анкеты исполнителей'})

class PerformersListView(ListView):
    model = Profile
    template_name = 'performers/all.html'  
    context_object_name = 'profiles'

    def get_queryset(self):
        return Profile.objects.filter(role='performer').order_by('id')