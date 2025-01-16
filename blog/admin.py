from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Tag, Category, Post, Comentario, Evento, Contato, Page
from django_summernote.admin import SummernoteModelAdmin
from .models import Post

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
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('title', 'is_published', 'created_at', 'updated_at', 'created_by', 'updated_by')
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'created_at', 'updated_at')
    list_per_page = 20
    ordering = ['-id']

    def link(self, obj):
        if not obj.pk:  
            return '-'
        url_do_post = obj.get_absolute_url()
        safe_link = mark_safe(f'<a href="{url_do_post}" target="_blank">Ver post</a>')
        return safe_link

    def save_model(self, request, obj, form, change):
        if change:
            obj.updated_by = request.user
        else:
            obj.created_by = request.user
        obj.save()

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

@admin.register(Page)
class PageAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('id', 'title', 'slug', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'slug')
    list_filter = ('is_published',)
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 10

