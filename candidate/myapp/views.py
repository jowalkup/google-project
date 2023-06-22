from django.shortcuts import render
from pygooglenews import GoogleNews
from django import template
register = template.Library()

def index(request):
    news = get_news('Kathy C. Hochul')
    context = {"news":news}
    return render(request, "tester.html", context)

def hello():
    print("hello")

def get_news(search):
    gn = GoogleNews(country = 'US')
    search = gn.search(search)
    newsitem = search['entries']

    news = []

    for item in newsitem:
        news.append({"title":item.title,"link":item.link})

    return news


# Create your views here.
