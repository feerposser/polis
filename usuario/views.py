from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

from .forms import FormUser, FormProfile, FormLogin, FormUserUpdate
from .models import ModelProfile


def login_profile(request):
    form = FormLogin(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            try:
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('user-profile')
            except Exception as e:
                print("\n\n", e, '\n\n')

    return render(request, 'blog/login.html', {'form': form})


def register_profile(request):
    if request.method == 'POST':
        try:
            form = FormUser(request.POST)

            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('user-profile')
            else:
                raise Exception
        except Exception:
            return render(request, 'blog/login.html', {'form': form})
    return render(request, 'blog/registrar.html')


@login_required()
def profile(request):
    if request.method == 'GET':
        user = request.user
        user_profile = ModelProfile.objects.get(usuario=user)

        form_profile = FormProfile(user_profile.get_dict_profile())
        form_user = FormUserUpdate(user_profile.get_dict_user())

        context = {'profile': user_profile,
                   'form_user': form_user,
                   'form_profile': form_profile}

        return render(request, 'usuario/user_settings.html', context)
