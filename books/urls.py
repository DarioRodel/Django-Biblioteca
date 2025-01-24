from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('authors/', views.authorlist, name='author_list'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),

    path('genres/', views.genre_list, name='genre_list'),
    path('genre/<int:genre_id>/', views.genre_detail, name='genre_detail'),

    path('authors1/',views.add_author, name='add_author'),

]
