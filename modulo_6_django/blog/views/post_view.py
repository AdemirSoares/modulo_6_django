from django.views import generic

from blog.models import Post


class PostView(generic.ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(status=1).order_by('-publish')


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'