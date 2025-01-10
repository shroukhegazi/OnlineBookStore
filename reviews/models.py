from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    book = models.ForeignKey(
        "books.Book", related_name="reviews", on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        "users.CustomUser", related_name="reviews", on_delete=models.CASCADE
    )
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        help_text="Rating must be between 0 and 10.",
    )
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.book.title}"
