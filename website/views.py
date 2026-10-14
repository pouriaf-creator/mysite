from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


def index_view(requset):
    return render(requset,'website/index.html')

def about_view(requset):
    return render(requset,'website/about.html')


def contact_view(requset):
    return render(requset,'website/contact.html')
