from django.shortcuts import render


def index(request):
    return render(request, 'infraestrutura/base_infraestrutura.html')
