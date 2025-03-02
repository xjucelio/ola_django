from django.shortcuts import render  # type: ignore

# Create your views here.


def home(request):
    print('home')

    context = {
        'text': 'Ola home'
    }
    return render(
        request,
        'home/index.html',
        # 'global/base.html'
        context

    )
