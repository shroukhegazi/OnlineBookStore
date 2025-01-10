from rest_framework import generics
from .models import Book
from .serializers import BookListSerializer, BookDetailSerializer
from rest_framework.permissions import IsAuthenticated


class BookListView(generics.ListAPIView):
    """
    View to list all available books.
    """

    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    permission_classes = [IsAuthenticated]


class BookDetailView(generics.RetrieveAPIView):
    """
    View to retrieve details of a specific book.
    """

    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    permission_classes = [IsAuthenticated]
