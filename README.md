# eAttendance

Simple Django app for signing up, logging in, and tracking attendance sessions with a lightweight SQLite database and Bootstrap UI.

## Introduction

The project provides a minimal authentication flow built with Django 4.2. It stores user profiles in SQLite, hashes passwords on signup, and uses session data to show logged-in state in the UI. Templates live in `auth_app/templates` and share a common Bootstrap layout via `base.html`.

## Setup

1. Install prerequisites: Python 3.10+ and `pip`.
2. (Recommended) Create and activate a virtual environment:
   - `python -m venv .venv`
   - `source .venv/bin/activate` (Linux/macOS) or `.venv\Scripts\activate` (Windows)
3. Install dependencies:
   - `pip install "django==4.2.7"`
4. Apply database migrations:
   - `python manage.py migrate`
5. (Optional) Create an admin user if you plan to use Django admin:
   - `python manage.py createsuperuser`

## Usage

- Start the dev server with `python manage.py runserver` and open `http://127.0.0.1:8000/`.
- From the landing page, choose **Signup** to create an account; passwords are hashed before storage.
- Log in via **Login**; the navbar will show the active user session.
- Use **Logout** in the navbar to clear the session.

## Notes

- The default database is SQLite (`db.sqlite3`) located in the project root; no extra setup is required for local development.
- Static assets are loaded from Bootstrap CDN; no build step is needed.
