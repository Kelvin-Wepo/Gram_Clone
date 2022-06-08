"""Posts Views"""

# Django
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.http import HttpResponse

# Models
from post.models import Post

# Forms
from post.forms import PostForm


# LoginRequired into Views
class CreatePostView(LoginRequiredMixin, CreateView):
    """Create New Post View"""
    template_name = 'post/new.html'
    form_class = PostForm
    success_url = reverse_lazy('post:feed')
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        """Add User and profile to context."""
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user.profile
        return context


class PostFeedView(ListView):
    """Return all published posts."""
    template_name = 'post/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 4
    context_object_name = 'posts'


class PostDetailView(DetailView):
    """Detail view posts"""
    template_name = 'post/detail.html'
    slug_field = 'id'
    slug_url_kwarg = 'post_id'
    queryset = Post.objects.all()
    context_object_name = 'post'
