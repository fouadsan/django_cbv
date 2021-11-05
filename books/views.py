from django.shortcuts import render
from django.views.generic.base import TemplateView
from  django.views.generic.detail import DetailView
from django.db.models import F
from django.utils import timezone

from .models import Book


class IndexView(TemplateView):

    template_name = "books/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context


class BookDetailView(DetailView):

    model = Book
    
    # Additional stuff:
    
    template_name = "books/book-detail.html"  # must include it if not the same name 
    context_object_name = 'book' # in html {{book.title}}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = Book.objects.filter(slug=self.kwargs.get('slug'))
        book.update(count=F('count') + 1)
        context['time'] = timezone.now()
        return context