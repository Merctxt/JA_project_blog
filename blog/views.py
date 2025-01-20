from django.shortcuts import render, redirect
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .models import Page
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Post, Category, Tag, Evento
from .forms import ComentarioForm, ContatoForm

# Views (definições iniciais renderizando templates)
def index(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_at', '-id')
    eventos = Evento.objects.all().order_by('data')[:8]
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request,
          'blog/index.html',
            {
                'posts': page_obj,
                  'page_obj': page_obj,
                    'eventos': eventos
                    })

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)
    category = post.category
    tags = post.tags.all() if post.tags.exists() else []
    comentarios = post.comentarios.all().order_by('-data_criacao')

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.autor = request.user
            comentario.save()
            messages.success(request, 'Comentário enviado com sucesso!')
            return redirect(post.get_absolute_url())
    else:
        form = ComentarioForm()

    return render(
        request,
          'blog/post_detail.html',
            {
                'post': post,
                  'category': category,
                    'tags': tags,
                      'comentarios': comentarios,
                         'form': form,
                            'page_title': post.title
        }
    )

def page(request, slug):
    page = get_object_or_404(Page, slug=slug, is_published=True)
    return render(request, 'blog/page.html', {'page': page, 'page_title': page.title})

def base_context(request):
    pages = Page.objects.filter(is_published=True)
    return {'pages': pages}

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
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('blog:contact')
    else:
        form = ContatoForm()

    return render(request, 'blog/contact.html', {'form': form})  # Página de contato

def events(request):
    eventos = Evento.objects.filter(is_published=True).order_by('data')
    return render(request, 'blog/events.html', {'eventos': eventos})  # Página de eventos

def login_view(request):
    return render(request, 'blog/login.html')  # Página de login

def register(request):
    return render(request, 'blog/register.html')  # Página de registro

def user_update(request):
    return render(request, 'blog/user_update.html')  # Atualização de perfil

def logout_view(request):
    return render(request, 'blog/login.html')  # Logout

