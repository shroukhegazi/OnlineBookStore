from rest_framework import generics
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from books.models import Book
from rest_framework.exceptions import NotFound


class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all().select_related("book", "user")
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        book_id = self.kwargs["book_id"]
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            raise NotFound(detail="Book not found.")

        serializer.save(user=self.request.user, book=book)

    def get_queryset(self):
        book_id = self.kwargs["book_id"]
        return (
            Review.objects.filter(book_id=book_id)
            .select_related("book", "user")
            .order_by("-created_at")
        )
