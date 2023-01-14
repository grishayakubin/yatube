from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    title = 'Это главная страница проекта Yatube'
    template = 'posts/index.html'
    context = {'title' : title}
    return render(request, template, context)

def group_posts(request, slug):
    title = 'Здесь будет информация о группах проекта Yatube'
    template = 'posts/group_list.html'
    context = {'text' : title}
    return render(request, template, context, slug)