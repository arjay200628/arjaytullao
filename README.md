# Django Portfolio Project

This is a simple Django portfolio website built with beginner-friendly HTML templates.

## How to run the project

1. Open a terminal in the project root folder (`myproject`).
2. Make sure you have Python installed.
3. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

4. Install Django if it is not already installed:

   ```bash
   pip install django
   ```

5. Run the Django development server:

   ```bash
   python manage.py runserver
   ```

6. Open your browser and visit:

   ```text
   http://127.0.0.1:8000/
   ```

## Project structure

- `manage.py` — Django command-line utility.
- `myproject/` — Django project settings and URL configuration.
- `templates/` — HTML templates used by the site.
- `static/` — static files like CSS or JS (if needed).

## Notes

- This project uses Django template inheritance with `base.html`.
- No external CSS file is required; styles are included inside the HTML templates.
