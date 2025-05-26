from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Defina as opções de status aqui
STATUS_CHOICES = [
    ('draft', 'Rascunho'),
    ('published', 'Publicado'),
]


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)
