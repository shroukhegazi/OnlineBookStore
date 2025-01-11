# OnlineBookStore

The Online Book Store is a simple and secure platform for book lovers to explore a curated collection and share reviews. Anyone can sign up, browse books, and contribute their thoughts to the community.

## Features
- User Management:
    - Any user can register and become a user.
    - User login to browse books and reviews

- Book Interaction:
   - View a list of available books in the store.
   - Access detailed information about each book, including its contents.

- Review System:
    - Read reviews submitted by others for any book.
    - Submit reviews about a book.

## Deliverables

- Django and DRF (Django Rest framework)
- PostgreSQL
- Unit tests (pytest)
- Docker and Docker-compose
- GitHub Actions
- Postman API Documentation

## Getting Started
### How to run the project

1. **`You should have docker and docker-compose installed`**
2. **`Clone the repo`**
   ```sh
   git clone https://github.com/shroukhegazi/OnlineBookStore
   ```
3. **`Go in the directory at the same level as docker-compose`**

4. **`Build images`**
   ```sh
   make build
   ```
5. **`Migrate models`**
   ```sh
   make migrate
   ```
6. **`Run the project`**
   ```sh
   make up
   ```
**`Create a superuser`**
   ```sh
   make createsuperuser
   ```
**`Run the tests and make a coverage report`**
   ```sh
   make test_coverage
   ```
## API Endpoints

### User Operations

- **`POST /users/auth/users/`**
  User Registration

- **`POST /users/auth/jwt/create/`**
  User Login

### Book Operations

- **`GET /books/`**
  List all books.

- **`GET /books/{book_id}`**
  Retrieve a book by its ID.

### Reviews Operations

- **`GET /books/{book_id}/reviews/`**
  List all reviews of a specific book.

- **`POST  /books/{book_id}/reviews/`**
  Create a book review.


## Documentation

### Postman Documentation

For detailed API requests and responses, visit the [Postman Documentation](https://documenter.getpostman.com/view/27281655/2sAYQWJt9e).
