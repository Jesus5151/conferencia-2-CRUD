from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
from .models import Book
from .forms import BookForm


def home(request):
    return render(request, 'base.html')


def book_list(request):
    books = Book.objects.filter()
    return render(request, 'book_list.html', {'books': books})



def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm()
    return render(request, 'create_book.html', {'form': form})



def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm(instance=book)
    return render(request, 'update_book.html', {'form': form, 'book': book})



def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('books')
    return render(request, 'delete_book.html', {'book': book})