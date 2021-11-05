from typing import List
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.db.models import F
from django.utils import timezone

from .models import Book
from .forms import AddForm


# class AddBookView(FormView): ex: Sending Email
#     template_name = 'add.html'
#     form_class = AddForm
#     success_url = '/books/'

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


class AddBookView(CreateView):  # used for saving object to db

    model = Book
    form_class = AddForm
    success_url = '/books/'
    template_name = 'add.html'
    success_url = '/books/'

    # def get_initial(self, *args, **kwargs):
    #     initial = super().get_initial(**kwargs)
    #     initial['title'] = 'Enter Title'
    #     return initial


class BookEditView(UpdateView):  # used for saving object to db

    model = Book
    form_class = AddForm
    success_url = '/books/'
    template_name = 'add.html'
    success_url = '/books/'


class IndexView(ListView):

    model = Book
    template_name = "home.html"
    context_object_name = "books"  # default = "object_list"
    paginate_by = 2
    # queryset = Book.objects.all()[:2]

    def get_queryset(self):
        return Book.objects.all()


class GenreView(ListView):

    model = Book
    template_name = "home.html"
    context_object_name = "books"  # default = "object_list"
    paginate_by = 2

    def get_queryset(self):
        return Book.objects.filter(genre__icontains=self.kwargs.get('genre'))


class BookDetailView(DetailView):

    model = Book

    # Additional stuff:

    # must include it if not the same name  default = "book_detail.html"
    template_name = "book-detail.html"
    context_object_name = 'book'  # in html {{book.title}}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = Book.objects.filter(slug=self.kwargs.get('slug'))
        book.update(count=F('count') + 1)
        context['time'] = timezone.now()
        return context
