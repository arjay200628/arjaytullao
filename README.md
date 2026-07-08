# Django Portfolio Project

This is a beginner-friendly Django portfolio website that uses a database to display personal information and projects.

## Features

- Home page
- About Me page
- Personal Information page
- Projects list page
- Project detail page
- Contact page
- Database-backed content using Django models

## How to run the project

1. Open a terminal in the project root folder.
2. Make sure Python is installed.
3. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

4. Install Django if needed:

   ```bash
   pip install django
   ```

5. Apply migrations:

   ```bash
   python manage.py migrate
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

7. Open your browser and visit:

   ```text
   http://127.0.0.1:8000/
   ```

## Project structure

- `manage.py` — Django command-line utility
- `myproject/` — Project settings, URLs, views, and models
- `templates/` — HTML templates for each page
- `static/` — Static files such as CSS and JavaScript

## Notes

- The project uses function-based views.
- The portfolio content is stored in the database through Django models.
- The project detail page shows the project description and a clickable link.
