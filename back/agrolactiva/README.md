# This is the read me file for how to run the django project

1. First go to the back folder and create a new virtual environment with the following commad and activate it

```bash
cd back/agrolactiva
python -m venv .venv
source .venv/bin/activate (For unix users)
.venv/Scripts/activate (For windows users)
```

3. The install the dependencies

```bash
pip install -r requirements.txt
```

4. Create migrations and migrate

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create superuser

```bash
python manage.py createsuperuser
```

6. Run the server

```bash
python manage.py runserver
```

7. Open the url address of the project and go to the following direction for login 127.0.0.1/api-auth/login

8. For admin go to the following url 127.0.0.1/admin
