# coding=utf-8
# -*- coding:utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.conf.urls import include, url
from django.views.generic import *
from django.views.generic.edit import *
from bookmanagement.models import *
from django.core.urlresolvers import reverse_lazy


# todo to reorganize the construct to extend the restful operation

class RestView(object):
    ''' > 抽象大法好! '''


    def __init__(self,model=None,field=None,success_url=None):
        self.model = model
        self.field = field
        self.success_url = success_url or '../..'



    def urlGroup(self):
        return include([url(r'^$',self.asList().as_view()),
                        url(r'^create$',self.asCreate().as_view()),
                        url(r'^update/(?P<pk>\d+)/$',self.asUpdate().as_view()),
                        url(r'^delete/(?P<pk>\d+)/$',self.asDelete().as_view())])

    def asList(self):
        t_model = self.model
        class List(ListView):
            model = t_model

        return List


    def asCreate(self):
        t_model = self.model
        t_field = self.field
        t_success_url = self.success_url

        class Create(CreateView):
            model = t_model
            fields = t_field
            success_url = './'

        return Create

    def asUpdate(self):
        t_model = self.model
        t_field = self.field
        t_success_url = self.success_url

        class Update(UpdateView):
            model = t_model
            fields = t_field
            success_url = t_success_url
            template_name_suffix = '_update_form'

        return Update

    def asDelete(self):
        t_model = self.model
        t_success_url = self.success_url

        class Delete(DeleteView):
            model = t_model
            success_url = t_success_url

        return Delete


#
# class BookView(RestView):
#     model = Book
#     fields = ['ISBN', "Title", "Publisher", "PublishDate", "Author", "Price"]
#     success_msg = "Book Created!"
#
#
# class BookList(ListView):
#     model = Book
#
#
# class BookCreate(CreateView):
#     model = Book
#     fields = ['ISBN', "Title", "Publisher", "PublishDate", "Author", "Price"]
#     success_msg = "Book Created!"
#
#
# class BookUpdate(UpdateView):
#     model = Book
#     fields = ['ISBN', "Title", "Publisher", "PublishDate", "Author", "Price"]
#     template_name_suffix = '_update_form'
#
#
# class BookDetail(DetailView):
#     model = Book
#
#
# class AuthorList(ListView):
#     model = Author
#
#
# class AuthorCreate(CreateView):
#     model = Author
#     fields = ["Name", "Age", "Country"]
#     success_msg = "Author Created!"
#
#
# class AuthorUpdate(UpdateView):
#     success_url='../..'
#     model = Author
#     fields = ["Name", "Age", "Country"]
#     template_name_suffix = '_update_form'
