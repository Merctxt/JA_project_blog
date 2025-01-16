from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Page
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Post

# Views (definições iniciais renderizando templates)
def index(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_at', '-id')
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/index.html', {'posts': page_obj, 'page_obj': page_obj})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug, is_published=True)
    return render(request, 'blog/post_detail.html', {'post': post})

def page(request, slug):
    page = get_object_or_404(Page, slug=slug, is_published=True)
    return render(request, 'blog/page.html', {'page': page})

def CategoryList(request, slug):
    ...

def TagList(request, slug):
    ...

def SearchList(request):
    ...

def contact(request):
    return render(request, 'blog/contact.html')  # Página de contato

def events(request):
    return render(request, 'blog/events.html')  # Página de eventos

def login_view(request):
    return render(request, 'blog/login.html')  # Página de login

def register(request):
    return render(request, 'blog/register.html')  # Página de registro

def user_update(request):
    return render(request, 'blog/user_update.html')  # Atualização de perfil

def logout_view(request):
    return render(request, 'blog/login.html')  # Logout

