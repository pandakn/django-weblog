from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post
from .forms import ContactForm
from django.db.models import Q

def home(request):
    # Query all posts
    all_posts = Post.objects.all()
    return render(request, 'blog/home.html', {'all_posts': all_posts})


def single_post(request, slug):
    # Query only post
    single_post = Post.objects.get(slug=slug)
    return render(request, 'blog/single-post.html', {'single_post': single_post})


def contact(request):
    # Check the incoming method
    if request.method == 'POST':
        # print('This is POST')
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()        # save into db
            return redirect('/')  # Redirect to home page
    else:
        # print('This is GET')
        form = ContactForm()


    return render(request, 'blog/contact.html', {'form': form})


def search(request):
    search_post = request.GET.get('q')
    if search_post:
        posts = Post.objects.filter(Q(title__icontains=search_post))
    else:
        return redirect('/')
    return render(request, 'blog/search.html', {'posts': posts})