# Blogging Platform

Blogging Platform for E6 Data Interview Test

## Technichal stack used

- **Django Rest Framework**
- **SQLite**
- **Unit Testing**
- **Swagger**


## Authentication Endpoints

### Authenticate User (POST)

- **Endpoint:** `/auth/login/`
- **Request Body:**
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```

### Register User (POST)

- **Endpoint:** `/auth/register/`
- **Request Body:**
  ```json
  {
    "email": "email",
    "username": "new_username",
    "first_name": "first_name",
    "last_name": "last_name",
    "password": "new_password"
  }
  ```

## Blog Endpoints

### List Blogs (GET)

- **Endpoint:** `/blogs/`

### Create Blog (POST)

- **Endpoint:** `/blogs/`
- **Request Body:**
  ```json
  {
    "title": "Blog Title",
    "content": "Blog Content"
  }
  ```

### Read Blog (GET)

- **Endpoint:** `/blogs/{id}/`

### Update Blog (PUT)

- **Endpoint:** `/blogs/{id}/`
- **Request Body:**
  ```json
  {
    "title": "Updated Title",
    "content": "Updated Content"
  }
  ```

### Partial Update Blog (PATCH)

- **Endpoint:** `/blogs/{id}/`
- **Request Body:**
  ```json
  {
    "content": "Updated Content"
  }
  ```

### Delete Blog (DELETE)

- **Endpoint:** `/blogs/{id}/`

### Filter Blog by author (GET)

- **Endpoint:** `/blogs/?author=authorname`

### Filter Blog by Create Date (GET)

- **Endpoint:** `/blogs/?pub_date=published_date`

## Getting Started

1. Clone the repository: ``
2. Navigate to the project directory: `cd Blog`
3. Set up a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. CD blogapi/
7. Apply migrations: `python manage.py migrate`
8. Run the development server: `python manage.py runserver`

Now, the Django Blogging Platform is up and running. You can access the API endpoints as described above.

## Documentation

For detailed documentation on each endpoint, including request and response formats, explore the Swagger documentation. Start the development server and visit `http://127.0.0.1:8000/swagger/` in your browser.