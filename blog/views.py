from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Page

# Views (definições iniciais renderizando templates)
def index(request):
    return render(request, 'blog/index.html')  # Página inicial

def post_detail(request, slug):
    return render(request, 'blog/post_detail.html')  # Detalhes do post

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

