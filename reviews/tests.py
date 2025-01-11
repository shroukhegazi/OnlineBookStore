import pytest
from rest_framework.test import APIClient
from reviews.models import Review
from books.models import Book
from users.models import CustomUser


# Fixtures
@pytest.fixture
def user():
    return CustomUser.objects.create_user(
        username="testuser", email="testuser@example.com", password="testpassword"
    )


@pytest.fixture
def book():
    return Book.objects.create(
        title="Test Book", author="Test Author", published_date="2025-01-01"
    )


@pytest.fixture
def reviews(book, user):
    return [
        Review.objects.create(
            book=book,
            user=user,
            rating=rating,
            review_text=f"Review {rating}",
        )
        for rating in range(1, 6)  # Create reviews with ratings 1 to 5
    ]


@pytest.fixture
def api_client():
    return APIClient()


# Test Cases
@pytest.mark.django_db
def test_list_reviews_authenticated(api_client, user, book, reviews):
    """
    Test listing reviews for a book as an authenticated user.
    """
    api_client.force_authenticate(user=user)
    response = api_client.get(f"/books/{book.id}/reviews/")
    assert response.status_code == 200

    data = response.json()
    assert len(data["results"]) == len(reviews)

    # Order reviews to match the API response
    sorted_reviews = sorted(reviews, key=lambda r: r.created_at, reverse=True)

    assert data["results"][0]["review_text"] == sorted_reviews[0].review_text
    assert data["results"][1]["rating"] == sorted_reviews[1].rating


@pytest.mark.django_db
def test_list_reviews_unauthenticated(api_client, book, reviews):
    """
    Test listing reviews for a book as an unauthenticated user.
    """
    response = api_client.get(f"/books/{book.id}/reviews/")
    assert response.status_code == 401


@pytest.mark.django_db
def test_create_review_authenticated(api_client, user, book):
    """
    Test creating a review for a book as an authenticated user.
    """
    api_client.force_authenticate(user=user)
    payload = {"rating": 8, "review_text": "Great book!"}
    response = api_client.post(f"/books/{book.id}/reviews/", payload)
    assert response.status_code == 201

    review = Review.objects.get(book=book, user=user, review_text="Great book!")
    assert review.rating == 8
    assert review.review_text == "Great book!"


@pytest.mark.django_db
def test_create_review_with_invalid_rating(user, book, api_client):
    """
    Test creating a review with an invalid rating (greater than 10).
    """
    api_client.force_authenticate(user=user)

    # Data for the review with an invalid rating
    review_data = {
        "rating": 11,
        "review_text": "This book was amazing!",
    }

    response = api_client.post(f"/books/{book.id}/reviews/", review_data)

    assert response.status_code == 400


@pytest.mark.django_db
def test_create_review_unauthenticated(api_client, book):
    """
    Test creating a review for a book as an unauthenticated user.
    """
    payload = {"rating": 7, "review_text": "Interesting read"}
    response = api_client.post(f"/books/{book.id}/reviews/", payload)
    assert response.status_code == 401


@pytest.mark.django_db
def test_list_reviews_nonexistent_book(api_client, user):
    """
    Test listing reviews for a nonexistent book.
    """
    api_client.force_authenticate(user=user)
    response = api_client.get("/books/999/reviews/")
    assert response.status_code == 200
    data = response.json()
    assert len(data["results"]) == 0
