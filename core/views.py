from django.shortcuts import render
from books.models import Category, Books
# Create your views here.
def home(request, id=None):
    cat = Category.objects.all()
    if id == None:
        books = Books.objects.all()
    else:
        books = Books.objects.filter(category__id = id)
    print(books)
    return render(request, 'index.html', {'cat': cat, 'books': books })