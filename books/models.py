from django.db import models
from users.models import CustomUser


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    book_file = models.FileField(upload_to="books/", null=True, blank=True)

    readers = models.ManyToManyField(CustomUser, related_name="read_books", blank=True)

    def __str__(self):
        return self.title
