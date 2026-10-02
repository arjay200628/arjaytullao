# Personal Portfolio with Admin Dashboard

This is a Django-based personal portfolio website with public portfolio pages and an admin-only dashboard for managing projects and tech stacks.

## Features

- Portfolio homepage and portfolio sections
- About me and personal information pages
- Project list and project detail pages
- Contact form and testimonials
- Superuser-only login page
- Register page for creating a user account
- Dashboard with:
  - Project table list
  - Tech stack table list
  - Create Project form
  - Create Tech Stack form
- Reusable TechStack model so the same stack can be used across multiple projects without duplication

## Tech Stack

- Python
- Django
- SQLite
- Bootstrap 5
- HTML/CSS

## Project Structure

- `manage.py` — Django project entry point
- `myproject/` — app settings, views, models, URLs, forms, and migrations
- `templates/` — HTML templates for the site and dashboard
- `static/` — static files such as CSS and JavaScript
- `.env.example` — example environment variables
- `.gitignore` — excludes local environment and database files

## Setup Instructions

1. Clone the repository.
2. Open a terminal in the project root.
3. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

4. Install Django:

   ```bash
   pip install django
   ```

5. Create your local environment file:

   ```bash
   copy .env.example .env
   ```

   Then update `.env` with your own values:

   ```env
   SECRET_KEY=replace-with-your-secret-key
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

6. Run the database migrations:

   ```bash
   python manage.py migrate
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

8. Open the project in the browser:

   ```text
   http://127.0.0.1:8000/
   ```

## Admin Access

Create a superuser account:

```bash
python manage.py createsuperuser
```

Then open the admin sign-in page:

```text
http://127.0.0.1:8000/admin-login/
```

Only superusers can log in here. Regular users are blocked.

## Sign Up Page

A user registration page is available here:

```text
http://127.0.0.1:8000/register/
```

This is for creating a regular user account. The login page still only accepts superusers.

## Dashboard

After logging in as the admin, open:

```text
http://127.0.0.1:8000/dashboard/
```

The dashboard includes:

- A table of all projects
- A table of all tech stacks
- Create Project button
- Create Tech Stack button

## Database Notes

This project uses a normalized `TechStack` model with a many-to-many relationship to `Project`, which allows each tech stack to be reused across multiple projects without creating duplicates.

## Repository Hygiene

The repository is set up for a clean clone and does not include local environment files or the SQLite database in Git. The following are ignored:

- `.venv/`
- `db.sqlite3`
- `.env`
- `__pycache__/`
- editor-specific folders

## Notes

- The public portfolio pages continue to reflect the project records in the database.
- New projects with associated tech stacks will appear in the portfolio and in the dashboard automatically.
- Keep your local `.env` file private and do not commit secrets or credentials.
