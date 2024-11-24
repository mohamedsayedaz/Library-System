from django.test import TestCase
from django.urls import reverse
from .models import Book


def BookTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Book Title",
            subtitle="Book Subtitle",
            author="Book Author",
            isbn="1233",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "Book Title")
        self.assertEqual(self.book.subtitle, "Book Subtitle")
        self.assertEqual(self.book.author, "Book Author")
        self.assertEqual(self.book.isbn, "1233")

    def test_book_list_view(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Book Subtitle")
        self.assertTemplateUsed(response, "books/book_list.html")
