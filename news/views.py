from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Hello world!')


def test(request):
    return HttpResponse('<h1>Test page</h1>')
