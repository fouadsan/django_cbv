from django.views.generic.base import TemplateView, RedirectView
from django.shortcuts import get_object_or_404
from django.db.models import F

from .models import Post

class Ex2View(TemplateView):
    template_name = "ex2.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.get(id=1)
        context['data'] = "Context Data for Ex2"
        return context


class PostPreLoadTaskView(RedirectView):
    # url = 'htttp://youtube.com' or:
    pattern_name = 'cbv:singlepost'
    # permanent = HTTP status code returned (True = 301, False = 302, Default = False) for the SEO
    
    def get_redirect_url(self, *args, **kwargs):
        # post = get_object_or_404(Post, pk=kwargs['pk'])
        # post.count = F('count') + 1
        # post.save()

        post = Post.objects.filter(pk=kwargs['pk'])
        print(post.count)
        post.update(count=F('count') + 1)

        return super().get_redirect_url(*args, **kwargs)
    
    
class SinglePostView(TemplateView):
    template_name = "ex4.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        return context