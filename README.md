<h1 align="center"> Dhanus Tech Fest Website</h1>

This is the official website for the Dhanus Tech Fest.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/dhanus-tech-fest/dhanus-website
```


2. Create a virtual environment and activate it:

```bash
virtualenv env
source env/bin/activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Migrate the database:
```bash
python manage.py migrate
```

5. Create a superuser:

```bash
python manage.py createsuperuser
```


6. Run the development server:
```bash
python manage.py runserver
```

The website should now be running at `http://localhost:8000`.

## Features

- View all events and their details
- Add new events to the website
- Edit existing events
- Retrieve events via a JSON API

