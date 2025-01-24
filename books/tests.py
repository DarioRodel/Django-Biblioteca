from django.test import TestCase
from books.models import Author, Genre, Book
from datetime import date
from django.urls import reverse


class AuthorTests(TestCase):

    def setUp(self):
        self.author = Author.objects.create(first_name='Dario', last_name='Romero', birth_date=date(2000, 1, 1))

    def test_author_creation(self):
        self.assertEqual(self.author.first_name, 'Dario')
        self.assertEqual(self.author.last_name, 'Romero')
        self.assertEqual(str(self.author), "Dario Romero")


class GenreTests(TestCase):

    def setUp(self):
        self.genre = Genre.objects.create(name='Drama')

    def test_genre_creation(self):
        self.assertEqual(self.genre.name, 'Drama')
        self.assertEqual(str(self.genre), "Drama")


class BookTests(TestCase):

    def setUp(self):
        self.author = Author.objects.create(first_name="Dario", last_name="Romero", birth_date=date(2000, 1, 1))
        self.genre = Genre.objects.create(name="Drama")
        self.book = Book.objects.create(
            title='Madridistas',
            genre=self.genre,
            publish_date=date(2000, 1, 1),
            summary='Vamos Madrid',
        )
        self.book.author.add(self.author)

    def test_book_creation(self):
        self.assertEqual(self.book.title, 'Madridistas')
        self.assertEqual(self.book.genre, self.genre)
        self.assertIn(self.author, self.book.author.all())


class ViewTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(first_name="Dario", last_name="Romero", birth_date=date(2000, 1, 1))
        self.genre = Genre.objects.create(name="Drama")
        self.book = Book.objects.create(
            title='Madrid',
            genre=self.genre,
            publish_date=date(2000, 1, 1),
            summary='Vamos Madrid',
            author=self.author,
        )
























    def test_book_list_view(self):
        response = self.client.get(reverse('books:book-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.book.title)

    def test_author_list_view(self):
        response = self.client.get(reverse('books:author-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.author.first_name)

    def test_book_detail_view(self):
        response = self.client.get(reverse('books:book-detail', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.book.title)
        self.assertContains(response, self.author.first_name)
