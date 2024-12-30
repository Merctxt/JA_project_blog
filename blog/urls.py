from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    # URLs relacionadas aos posts
    path('', views.index, name='index'),  # Página inicial com lista de posts
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),  # Detalhes do post

    # URLs para páginas estáticas e extras
    path('page/<slug:slug>/', views.page, name='page'),  # Página estática genérica
    path('contact/', views.contact, name='contact'),  # Página de contato
    path('events/', views.events, name='events'),  # Página de eventos
    path('tag/<slug:slug>/', views.TagList, name='tag_posts'),
    path('category/<slug:slug>/', views.CategoryList, name='category_posts'),

    # URLs relacionadas a usuários
    path('login/', views.login_view, name='login'),  # Página de login
    path('register/', views.register, name='register'),  # Página de registro
    path('user/update/', views.user_update, name='user_update'),  # Atualização de perfil
    path('logout/', views.logout_view, name='logout'),  # Logout
]
