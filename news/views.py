from django.http import HttpResponse
from news.models import News, Category


def index(request):
    news = News.objects.get(title='News 2')
    category = Category.objects.get(pk=1).news_set.all()
    return HttpResponse(category)


def test(request):
    return HttpResponse('<h1>Test page</h1>')


def din_var(request, value):
    return HttpResponse(f'<h1>Dynamically value is: {value}</h1>')
