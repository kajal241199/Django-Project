from django.shortcuts import render

posts = [
    {
        'author': 'Kajal Singhvi',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 22, 2021'
    },
    {
        'author': 'Deepak Singhvi',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'January 24, 2021'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

