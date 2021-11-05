from typing import List
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db.models import F
from django.utils import timezone

from .models import Book


class IndexView(ListView):

    model = Book
    template_name = "books/home.html"
    context_object_name = "books"  # default = "object_list"
    paginate_by = 2
    # queryset = Book.objects.all()[:2]

    def get_queryset(self):
        return Book.objects.all()[:2]


class GenreView(ListView):

    model = Book
    template_name = "books/home.html"
    context_object_name = "books"  # default = "object_list"
    paginate_by = 2

    def get_queryset(self):
        return Book.objects.filter(genre__icontains=self.kwargs.get('genre'))


class BookDetailView(DetailView):

    model = Book

    # Additional stuff:

    # must include it if not the same name  default = "book_detail.html"
    template_name = "books/book-detail.html"
    context_object_name = 'book'  # in html {{book.title}}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = Book.objects.filter(slug=self.kwargs.get('slug'))
        book.update(count=F('count') + 1)
        context['time'] = timezone.now()
        return context
