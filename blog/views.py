from django.shortcuts import render

posts = [
    {
        'author': 'AlexCS', 
        'title': 'Blog Post 1', 
        'content': 'First Post Content', 
        'date_posted': 'July 1, 2022'
    }, 
    {
        'author': 'Claxton Doe', 
        'title': 'Blog Post 2', 
        'content': 'Second Post Content', 
        'date_posted': 'July 4, 2022'
    }
]

def home(request): 
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request): 
    return render(request, 'blog/about.html', {'title': 'About'})

