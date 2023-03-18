from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('Главная страница')


def group_list(request):
    return HttpResponse('Названия групп')


def group_posts(request, slug):
    return HttpResponse(f'Записи сообщества {slug}')