from django.shortcuts import render
from pygooglenews import GoogleNews
from django import template
from django.shortcuts import render
register = template.Library()

candidateName = ""

def index(request):
    return render(request, "tester.html")

def get_news(search):
    gn = GoogleNews(country = 'US')
    search = gn.search(search)
    newsitem = search['entries']

    news = []

    for item in newsitem:
        news.append({"title":item.title,"link":item.link})

    return news

def button(request):
    return render(request,'tester.html')


def output(request):
    name = request.GET.get('name')
    news = get_news(name)
    context = {"news":news}    

    return render(request,"tester.html",context)


# Create your views here.
