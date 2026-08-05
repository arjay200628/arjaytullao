# Django Portfolio Project

This is a beginner-friendly Django portfolio website built for a Computer Engineering student project. It uses Django models and templates to display personal information, projects, testimonials, and a contact form.

## Features

- Home page with hero section, skills, and portfolio statistics
- About Me page with education and interests
- Personal Information page with user details
- Projects page with database-powered project cards
- Project detail page with project description and link
- Contact page with contact information and inquiry form
- Testimonials section with user-submitted feedback
- Clean Bootstrap 5 layout and responsive design

## Technologies

- Python 3
- Django
- SQLite
- Bootstrap 5
- Django templates

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

## Admin access

To manage models and add content through the Django admin site, create a superuser:

```bash
python manage.py createsuperuser
```

Then open:

```text
http://127.0.0.1:8000/admin/
```

## Project structure

- `manage.py` — Django command-line utility
- `myproject/` — Django application folder with settings, URLs, views, and models
- `templates/` — HTML templates used by views
- `static/` — Local static files
- `db.sqlite3` — SQLite database file

## Notes

- All styling uses Bootstrap 5 and inline `<style>` tags in templates.
- No external CSS files or JavaScript libraries were added.
- The backend logic, models, and URLs are unchanged by the visual redesign.
- Use the admin site to populate projects, testimonials, and personal information.
