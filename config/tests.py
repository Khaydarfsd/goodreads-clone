from django.test import TestCase
from django.urls import reverse

from books.models import Book, BookReview
from users.models import CustomUser


class HomePageTestCase(TestCase):
    def test_paginated_list(self):
        book = Book.objects.create(title='Book1', description='Description', isbn='123123')
        user = CustomUser.objects.create(
            username='khaydar', first_name='Khaydar', last_name='Tursunov', email='haydartursunov1@gmail.com'
        )
        user.set_password('somepass')
        user.save()
        review1 = BookReview.objects.create(book=book, user=user, stars_given=3, comment='Very good book')
        review2 = BookReview.objects.create(book=book, user=user, stars_given=4, comment='Nice book')
        review3 = BookReview.objects.create(book=book, user=user, stars_given=5, comment='Useful book')

        response = self.client.get(reverse('home_page') + '?page_size=2')

        self.assertContains(response, review3.comment)
        self.assertContains(response, review2.comment)
        self.assertNotContains(response, review1.comment)
