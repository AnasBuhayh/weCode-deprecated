# weCode
The source code of WeCode.ly blog

# Specifications
Framework: Django
Database: PostgreSQL

# Installation

### Database setup

Install PostgreSQL and create a database. The database info are found in weCode/settings.py

### App Setup

Clone the project to your preferred directory

`https://github.com/AnasBuhayh/weCode.git`

*Recomended:* Create a vistual environment

`python -m venv myEnv`

Run virtual environment

`.\myEnv\Scripts\activate`

Install requirements

`pip install -r .\requirements.txt`

Create superuser

`python manage.py createsuperuser`

Sync database

`python .\manage.py migrate --run-syncdb`

Run app

`python .\manage.py runserver`

