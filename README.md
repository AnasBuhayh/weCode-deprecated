# weCode - Deprecated
The source code of WeCode.ly blog. This website is currently being updated to incoporate Django REST.

# Features tutorial

[![image](https://github.com/AnasBuhayh/weCode-deprecated/assets/6984894/74eebaf4-cd04-4293-a347-3ab879fb95ed)](https://drive.google.com/file/d/1ZoT_s1rKJoPZz1q8ToY1EprMhUR06Omu/view?usp=drive_link)


# Specifications
- Framework: Django
- Database: PostgreSQL

# Installation

### Local database setup

- Create new Postgres database

### Development database setup

- Please email me at anas.buhayh@gmail.com if you would like to connect to the live database

### App Setup

- Clone the project to your preferred directory

`https://github.com/AnasBuhayh/weCode.git`

- Chenge the database variables to your newly created ones in the settings.py file

```
NAME = '[database name]'
USER = '[database user]'
PASSWORD = '[database password]'
HOST = 'localhost'
PORT = '5432'
```

- *Recomended:* Create a virtual environment

`python -m venv [env-name]`

- *Recomended:* Run virtual environment

`.\[env-name]\Scripts\activate`

- Install requirements

`pip install -r .\requirements.txt`

- Make migrations

`python manage.py makemigrations`

then

`python manage.py migrate`

- Create superuser

`python manage.py createsuperuser`

- Run application

`python ./manage.py runserver`
