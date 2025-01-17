from django.shortcuts import render, redirect
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .models import Page
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Post, Category, Tag

# Views (definições iniciais renderizando templates)
def index(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_at', '-id')
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/index.html', {'posts': page_obj, 'page_obj': page_obj})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)
    category = post.category
    tags = post.tags.all() if post.tags.exists() else []
    return render(
        request,
          'blog/post_detail.html',
            {'post': post, 'category': category, 'tags': tags, 'page_title': post.title})

def page(request, slug):
    page = get_object_or_404(Page, slug=slug, is_published=True)
    return render(request, 'blog/page.html', {'page': page})

def CategoryList(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category, is_published=True).order_by('-created_at')

    page_title = f'{category.name} - Categoria -'

    return render(request, 'blog/index.html', {'posts': posts, 'page_title': page_title})

def TagList(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags=tag, is_published=True).order_by('-created_at')

    page_title = f'{tag.name} - Tag -'

    return render(request, 'blog/index.html', {'posts': posts, 'page_title': page_title})

def SearchList(request):
    search_value = request.GET.get('search', '').strip()

    if not search_value:
        return redirect('blog:index')

    posts = Post.objects.filter(
        Q(title__icontains=search_value) | Q(content__icontains=search_value),
          is_published=True).order_by('-created_at')

    page_title = f'Search - {search_value[:20]}'

    return render(
        request,
          'blog/index.html',
            {'posts': posts, 'page_title': page_title, 'search_value': search_value})

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

