from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Category

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form, 'title': 'Регистрация'})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p = p_form.save()
            p.category = Category.objects.get(pk=p_form.cleaned_data['category'])
            p.save()

            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile, initial={'category': request.user.profile.category.id})

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'title': 'Профиль'
    }

    return render(request, 'profile.html', context)