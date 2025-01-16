from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from utils.rands import slugify_new
from utils.images import resize_image
from django_summernote.models import AbstractAttachment

# Modelo de Tag
class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    name = models.CharField(max_length=55)
    slug = models.SlugField(max_length=55, unique=True, default=None, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Page(models.Model):
    title = models.CharField(max_length=75)
    slug = models.SlugField(max_length=55, unique=True, default=None, null=True, blank=True)
    content = models.TextField()
    is_published = models.BooleanField(default=True, help_text='Marque para exibir no site')

    def get_absolute_url(self):
        if not self.is_published:
            return reverse('blog:index')
        return reverse('blog:page', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

# Modelo de Categoria
class Category(models.Model):
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    name = models.CharField(max_length=55)
    slug = models.SlugField(max_length=55, unique=True, default=None, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# Modelo de Post
class PostManager(models.Manager):
    def get_published(self):
        return self.filter(is_published=True).order_by('-id')

class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    objects = PostManager()

    title = models.CharField(max_length=75)
    slug = models.SlugField(max_length=55, unique=True, default=None, null=True, blank=True)
    content = models.TextField()
    excerpt = models.CharField(max_length=150)
    is_published = models.BooleanField(default=True, help_text='Marque para exibir no site')
    cover = models.ImageField(upload_to='posts/%Y/%m/', blank=True, default='')
    cover_in_post_content = models.BooleanField(default=True, help_text='Exibir imagem no conteúdo do post')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='post_created_by', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='post_updated_by', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, default=None, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True, default='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if not self.is_published:
            return reverse('blog:index')
        return reverse('blog:post', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title)

        current_cover_name = str(self.cover.name)
        super_save = super().save(*args, **kwargs)
        cover_changed = False

        if self.cover:
            cover_changed = current_cover_name != self.cover.name

        if cover_changed:
            resize_image(self.cover, 900, True, 75)

        return super_save

# Modelo de Comentário
class Comentario(models.Model):
    post = models.ForeignKey(Post, related_name='comentarios', on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.autor} no post {self.post}"

# Modelo de Evento
class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    data = models.DateField()
    descricao = models.TextField()

    def __str__(self):
        return self.titulo

# Modelo de Contato
class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensagem de {self.nome}"


class PostAttachment(AbstractAttachment):
    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.file.name
        
        current_file_name = str(self.file.name)
        super_save = super().save(*args, **kwargs)
        file_changed = False

        if self.file:
            file_changed = current_file_name != self.file.name

        if file_changed:
            resize_image(self.file, 900, True, 75)

        return super_save
