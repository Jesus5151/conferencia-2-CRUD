
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('books/', views.book_list, name='books'),
    path('books/create/', views.create_book, name='create_book'),
    path('books/update/<int:book_id>/', views.update_book, name='update_book'),
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'),
    


]
