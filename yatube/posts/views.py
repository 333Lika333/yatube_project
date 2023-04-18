from django.shortcuts import get_object_or_404, render

from .models import Group, Post

AMOUNT_OF_POSTS: int = 10


def index(request):
    posts = Post.objects.all()[:AMOUNT_OF_POSTS]
    title = 'Последние обновления на сайте'
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.select_related('author')[:AMOUNT_OF_POSTS]
    title = f'Записи сообщества {slug}'
    context = {
        'group': group,
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/group_list.html', context)
