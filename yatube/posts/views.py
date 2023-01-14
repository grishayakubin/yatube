from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)

def group_posts(request, slug):
    title = 'Здесь будет информация о группах проекта Yatube'
    template = 'posts/group_list.html'
    context = {'text' : title}
    return render(request, template, context, slug)