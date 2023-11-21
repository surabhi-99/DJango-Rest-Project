# Artist API Project Setup

The Artist API is a Django-based web application that provides endpoints for managing artists and their works. This README.md file contains step-by-step instructions on how to set up the project and how to call various APIs provided by the application.

## Project Setup

### Prerequisites

Before proceeding, ensure you have the following installed on your system:

1. Python (version 3.6 or higher)
2. pip (Python package manager)
3. Git (optional but recommended)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/surabhi-99/Django-REST-Project.git
   cd Django-REST-Project
   ```
   If you don't want to use Git, you can download the repository zip file from the GitHub page and extract it to a local directory.

2. Create a virtual environment:

   It's recommended to use a virtual environment to keep your project dependencies isolated.
   ```bash
   python3 -m venv venv # On macOS and Linux

   py -3 -m venv venv # On Windows
   ```
3. Activate the virtual environment:
    ```bash
   source venv/bin/activate # On macOS and Linux

   venv\Scripts\activate # On Windows
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Perform database migrations:
   ```bash
   python manage.py migrate
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```
   The API server should now be running at http://localhost:8000/.

## API Endpoints

### Register a new Artist

- **Endpoint:** `POST /api/register/`
- **Request Body:** Provide the name and password for the new artist
- **Authentication:** Not required (Open to the public)

### Retrieving a list of all works

- **Endpoint:** `GET /api/works/`
- **Authentication:** Required (User must be logged in)

### Create a new work

- **Endpoint:** `POST /api/works/`
- **Request Body:** Provide the link, work_type and artists for the new work
- **Authentication:** Required (User must be logged in)

### Search work with Work Type

- **Endpoint:** `GET /api/works/?work_type=work_type_name`
- **Replace `work_type_name` with the actual work type you want to search for. (eg. YT, IG, etc)**
- **Authentication:** Required (User must be logged in)

### Search work with Artist name

- **Endpoint:** `GET /api/works/?artist=artist_name`
- **Replace `artist_name` with the name of the artist you want to search for.**
- **Authentication:** Required (User must be logged in)

## Authentication and Permissions

- The API uses Token-based authentication. To access APIs that require authentication, you need to include an `Authorization` header in your requests with a valid token.
- To get a token, you can make a `POST` request to `/api/login/` with the valid credentials. The response will include an access token, which you can use for authenticated requests.
