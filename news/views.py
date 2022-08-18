from django.db.models import *
from django.http import HttpResponse
from news.models import News, Category


def index(request):
    # news = News.objects.aggregate(max_views=Min('views'), min_views=Max('views'))
    cat = Category.objects.all()
    return HttpResponse(news)


def test(request):
    return HttpResponse('<h1>Test page</h1>')


def din_var(request, value):
    return HttpResponse(f'<h1>Dynamically value is: {value}</h1>')
