from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


def index_view(requset):
    return HttpResponse('<h1> Home page </h1>')


def about_view(requset):
    return HttpResponse('<h1> About page </h1>')


def contact_view(requset):
    return HttpResponse('<h1> Contact page </h1>')
