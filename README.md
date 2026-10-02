# Django Portfolio Project

This portfolio project uses Django to display a personal portfolio, contact form, project catalog, and admin-only dashboard for managing projects and tech stacks.

## Features

- Home page with portfolio overview
- About Me and Personal Information pages
- Projects page with project cards and links
- Project detail page
- Testimonials and contact form
- Superuser-only dashboard for managing projects and tech stacks
- Dedicated admin login screen restricted to superusers only
- SQLite database with related TechStack and Project records

## Technologies

- Python 3
- Django
- SQLite
- Bootstrap 5
- Django templates

## Clean clone setup

After cloning the repo:

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Install project dependencies:

   ```bash
   pip install django
   ```

3. Copy the environment example file and set your values:

   ```bash
   copy .env.example .env
   ```

   Update the values in `.env` as needed. Example contents:

   ```env
   SECRET_KEY=replace-with-your-secret-key
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Open the site in your browser:

   ```text
   http://127.0.0.1:8000/
   ```

## Admin access

Create a superuser before logging into the admin-only dashboard:

```bash
python manage.py createsuperuser
```

Then sign in at:

```text
http://127.0.0.1:8000/admin-login/
```

Only superusers can authenticate on this page. Regular users are blocked.

## Dashboard

Once signed in as the admin, you can access:

```text
http://127.0.0.1:8000/dashboard/
```

The dashboard includes:

- Project list table
- Tech stack list table
- Create Project form
- Create Tech Stack form

## Repository hygiene

This project is set up to be cloned cleanly without committing local environment files:

- `.gitignore` excludes `.venv`, `db.sqlite3`, `.env`, and other local files
- `.env.example` is committed as a safe template without secrets
- Local database and virtual environment files are intentionally not stored in the repo

## Project structure

- `manage.py` — Django command-line utility
- `myproject/` — project settings, URLs, views, and models
- `templates/` — HTML templates for the site and dashboard
- `static/` — local static assets
- `.env.example` — sample environment variables
- `.gitignore` — git exclusions for local-only files

## Notes

- All styling uses Bootstrap 5 and template-based CSS.
- The admin-only dashboard is designed for project and tech stack management.
- The project uses a normalized `TechStack` model so the same stack can be reused across multiple projects without duplicates.
