from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.shortcuts import render
from .models import Book, Author, Genre
def index(request):
    book = Book.objects.all()
    return render(request, "books/index.html", {"books": book})
def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'books/author_detail.html', {'author': author})
def authorlist(request):
    authors = Author.objects.all()
    return render(request, "books/author_list.html", {"authors": authors})
def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "books/detail.html", {"book": book})
def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'books/genre_list.html', {'genres': genres})
def genre_detail(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
    return render(request, 'books/genre_detail.html', {'genre': genre})
def add_author(request):
    if request.method == 'POST':
        nombre=request.POST.get('nombre').strip()
        apellido=request.POST.get('apellido').strip()
        nacimiento=request.POST.get('nacimiento').strip()
        if nombre and apellido:
            new_author = Author(first_name=nombre, last_name=apellido, birth_date=nacimiento)
            new_author.save()
            return redirect('author_list')
    return render(request, 'books/add_author.html')

