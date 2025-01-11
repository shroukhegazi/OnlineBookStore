from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated


class BookListView(generics.ListAPIView):
    """
    View to list all available books.
    """

    queryset = Book.objects.all().order_by("-published_date")
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDetailView(generics.RetrieveAPIView):
    """
    View to retrieve details of a specific book.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
