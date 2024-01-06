from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from testapp.models import Book
from django.urls import reverse_lazy
# Create your views here.
class BookListView(ListView):
    model = Book
	#default template file:book_list.html
	#default context object name:book_list
class BookListView1(ListView):
    model = Book
    template_name = 'testapp/books.html'
    context_object_name = 'books'


class BookListView2(ListView):
    model = Book
    template_name = 'testapp/books.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name='testapp/books_details.html'



class BookCreateView(CreateView):
    model = Book
    # fields = ('title','author','pages','price')
    fields='__all__'

class BookUpdateView(UpdateView):
    model = Book
    # fields = ('pages','price')
    fields = '__all__'

class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('listbooks')


