from django.shortcuts import render
from django.views.generic import View, TemplateView
from  django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from classviewproject.models import Book
from django.urls import reverse_lazy

# Create your views here.

class HelloWorldView(View):
    def get(self,request):
        return HttpResponse("hello")

class HelloWorldTemplateView(TemplateView):
    template_name = 'classviewproject/test.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'durga'
        context['age'] = 34
        return context

# Model related view
#################
# ListView
# DetailView
# CreateView
# DeleteView
# UpdateView
################## 

class bookListView(ListView):
    model = Book   # this can be written as Book.objects.all()
    #default template willbe called always : (modelname_list.html) book_List.html
    #default context object :   book_list will be passed to templates.
    # context_object_name = 'list_of_books'   can be given custom context object 

class bookDetailView(DetailView):
    model = Book
    # it will talk about details of a particular book
    # default template name  : book_detail.html
    #default context : bookor object 

class bookCreateView(CreateView):
    model = Book
    fields=('title','author','pages','price')
    # fields=(__all__) Can be given too, If u want to require a book then u need all fields
    #default template name -- book_form

class bookUpdateView(UpdateView):
    model = Book
    fields=('title','price')

class bookDeleteView(DeleteView):
    model=Book
    # after deleting a record on which page i will go.
    success_url = reverse_lazy('bookList')