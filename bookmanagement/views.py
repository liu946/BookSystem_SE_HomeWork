from django.shortcuts import render

# Create your views here.
from django.views.generic import *
from django.views.generic.edit import *
from bookmanagement.models import *

class BookList(ListView):
    model = Book

class BookCreate(CreateView):
    model = Book
    fields = ['ISBN',"Title","Publisher","PublishDate","Author"]
    success_msg = "Book Created!"


class BookUpdate(UpdateView):
    model = Book
    fields = ['ISBN',"Title","Publisher","PublishDate","Author"]
    template_name_suffix = '_update_form'

class BookDetail(DetailView):
        model = Book

class AuthorList(ListView):
    model = Author

class AuthorCreate(CreateView):
    model = Author
    fields = ["Name","Age","Country"]
    success_msg = "Author Created!"

class AuthorUpdate(UpdateView):
    model = Author
    fields = ["Name","Age","Country"]
    template_name_suffix = '_update_form'