from django.shortcuts import render, redirect
from blogs.models import Category, Blog
from assignments.models import About
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


def home(request):
    featured_post = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    posts         = Blog.objects.filter(is_featured=False, status='Published')
    
    # Fetch about us
    try:
        about = About.objects.get()
    except:
        about = None
    
    context = {
        'featured_post': featured_post,
        'posts'        : posts,
        'about'        : about,
    }
    
    return render(request, 'home.html', context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)