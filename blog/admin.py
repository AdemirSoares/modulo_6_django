from django.contrib import admin

# Register your models here.
from .models import Post

<<<<<<< HEAD
admin.site.register(Post)
=======
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status", "created_on")
    list_filter = ("status",)
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)
>>>>>>> 7e72e91 (ajustes na documentação da branch django-admin)
