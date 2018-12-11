from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'welcome/index.html')


def tutorial(request):
    return HttpResponse('Heya Tutorial')


def game(request):
    return HttpResponse('Whoooooooooopps Game !')