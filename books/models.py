from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    book_file = models.FileField(upload_to="books/", null=True, blank=True)
    description = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.title
