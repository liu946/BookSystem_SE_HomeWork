from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from bookmanagement.models import *

class BookList(ListView):
    model = Book

class BookCreate(CreateView):
    model = Book
    fields = ['ISBN',"Title","Publisher","PublishDate","Author"]

class BookUpdate(UpdateView):
    model = Book
    fields = ['ISBN',"Title","Publisher","PublishDate","Author"]
    template_name_suffix = '_update_form'

class AuthorList(ListView):
    model = Author

class AuthorCreate(CreateView):
    model = Author
    fields = ["Name","Age","Country"]

class AuthorUpdate(UpdateView):
    model = Author
    fields = ["Name","Age","Country"]
    template_name_suffix = '_update_form'