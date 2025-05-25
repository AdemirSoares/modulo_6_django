from django.db import models
from django.contrib.auth.models import User

# Defina as opções de status aqui
STATUS_CHOICES = [
    ('draft', 'Rascunho'),
    ('published', 'Publicado'),
]


class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
