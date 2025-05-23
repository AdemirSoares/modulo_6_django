from django.ursl import path

from modulo_6_django.blog import views

urlpatterns = [
    path('', views.PostView.as_view(), name='home')
]