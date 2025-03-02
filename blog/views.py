from django.http.response import HttpResponse, Http404
from django.shortcuts import render  # type: ignore
from blog.data import posts
# from django.http import HttpResponse

# Create your views here.


def blog(request) -> HttpResponse:
    print('blog')

    context = {
        # 'text': 'Ola blog',
        'posts': posts
    }

    return render(
        request,
        'blog/index.html',
        context,
    )


def post(request, post_id):
    print('post', post_id)
    found_post = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post nao existe.')

    context = {
        # 'text': 'Ola blog',
        'post': found_post,
        'title': found_post['title'] + ' - ',
    }

    return render(
        request,
        'blog/post.html',
        context,
    )


def exemplo(request) -> HttpResponse:
    print('exemplo')

    context = {
        'text': 'Ola exemplo',
        'title': 'Pagina de exemplo - ',
    }

    return render(
        request,
        'blog/exemplo.html',
        context,
    )
