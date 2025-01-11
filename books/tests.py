import pytest
from rest_framework.test import APIClient
from books.models import Book
from users.models import CustomUser  # Replace with your actual model import


@pytest.fixture
def user():
    """
    Fixture to create a user for authentication.
    """
    return CustomUser.objects.create_user(
        username="testuser", email="testuser@example.com", password="testpassword"
    )


@pytest.fixture
def create_book():
    """
    Fixture to create a book instance.
    """
    return Book.objects.create(
        title="Test Book", author="Test Author", published_date="2025-01-01"
    )


@pytest.fixture
def multiple_books(db):
    """
    Fixture to create multiple book instances.
    """
    return Book.objects.bulk_create(
        [
            Book(title="Book 1", author="Author 1", published_date="2025-01-01"),
            Book(title="Book 2", author="Author 2", published_date="2025-02-01"),
            Book(title="Book 3", author="Author 3", published_date="2025-03-01"),
        ]
    )


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_list_paginated_books_authenticated(user, multiple_books, api_client):
    """
    Test listing multiple books with pagination for an authenticated user.
    """
    api_client.force_authenticate(user=user)
    response = api_client.get("/books/")

    assert response.status_code == 200
    data = response.json()
    # Order reviews to match the API response
    sorted_books = sorted(multiple_books, key=lambda r: r.published_date, reverse=True)

    assert data["count"] == len(sorted_books)
    assert data["results"][0]["title"] == sorted_books[0].title
    assert data["results"][1]["author"] == sorted_books[1].author


@pytest.mark.django_db
def test_book_list_unauthenticated(create_book, api_client):
    """
    Test unauthenticated access to book list.
    """
    response = api_client.get("/books/")
    assert response.status_code == 401


@pytest.mark.django_db
def test_book_detail_authenticated(user, create_book, api_client):
    """
    Test authenticated access to book detail.
    """
    api_client.force_authenticate(user=user)
    response = api_client.get(f"/books/{create_book.id}/")
    assert response.status_code == 200, (
        "Expected status code 200 for authenticated access"
    )
    data = response.json()
    assert data["title"] == create_book.title
    assert data["author"] == create_book.author
    assert data["published_date"] == str(create_book.published_date)


@pytest.mark.django_db
def test_book_detail_unauthenticated(create_book, api_client):
    """
    Test unauthenticated access to book detail.
    """
    response = api_client.get(f"/books/{create_book.id}/")
    assert response.status_code == 401
