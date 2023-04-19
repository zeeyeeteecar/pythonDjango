from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
    'author':'CoreyMS',
   'title':'Blog Post A',
   'content':'First post content',
   'date_posted':'August 27, 2018',
    },
    {
    'author':'Jane Doe',
   'title':'Blog Post B',
   'content':'2nd  post content',
   'date_posted':'August 27, 2018',
    },
]

def home(request):
    context = {
        'posts':posts 
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')


# Create your views here.
