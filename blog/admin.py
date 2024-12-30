from django.contrib import admin
from .models import Tag, Category, Post, Comentario, Evento, Contato

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    list_per_page = 20

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    list_per_page = 20

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'created_at', 'updated_at', 'created_by', 'updated_by')
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'created_at', 'updated_at')
    list_per_page = 20
    ordering = ['-id']

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('post', 'autor', 'texto', 'data_criacao')
    search_fields = ('texto', 'autor__username', 'post__title')
    list_filter = ('data_criacao',)
    list_per_page = 20
    ordering = ['-id']

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data', 'descricao')
    search_fields = ('titulo', 'descricao')
    list_per_page = 20
    ordering = ['-id']

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'mensagem', 'data_envio')
    search_fields = ('nome', 'email', 'mensagem')
    list_per_page = 20
    ordering = ['-id']
