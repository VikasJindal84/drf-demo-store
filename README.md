# drf-demo-store
This is demo project to show usage of Django REST framework

## ✨ Start the app in Docker

```bash
$ docker-compose up --build
```

- http://localhost:5005/api/swagger/ for swagger docs
- http://localhost:5005/admin for admin portal

<br />

## Manual Build

> 👉 Install modules via `VENV`

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> 👉 Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> 👉 Create app

```bash
$ python manage.py startapp app_name
```

<br />

> 👉 Start the app

```bash
$ python manage.py runserver
```

- At this point, the app runs at `http://127.0.0.1:8000/`.
- A swagger-ui view of your API specification at http://127.0.0.1:8000/api/swagger/
- A ReDoc view of your API specification at http://127.0.0.1:8000/api/redoc/
- http://127.0.0.1:8000/admin for admin portal

<br />
