# weCode
The source code of WeCode.ly blog

# Specifications
Framework: Django
Database: PostgreSQL

# Installation

## Database setup

- Create new Postgres database
- Restore the template database  `/database/default_db.sql`


### App Setup

- Clone the project to your preferred directory

`https://github.com/AnasBuhayh/weCode.git`

- *Recomended:* Create a vistual environment

`python -m venv myEnv`

- *Recomended:* Run virtual environment

`.\myEnv\Scripts\activate`

- Install requirements

`pip install -r .\requirements.txt`

- Add your newly created database name and credentials in the settings.py file

- Run application

`python ./manage.py runserver`

### django user credentials

username : admin
password : Admin_2020