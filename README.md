## YourStory

A story sharing platform using python Django framework where user can post a story. They can update and delete their post but only see and comment on others posts.


## Building

It is best to use the python `pipenv` tool to build locally:

```bash
> pip install pipenv
> pipenv sync
> git clone https://github.com/ifat-mohit/YourStory.git
```
## Creating Database and Tables

You make migrations to the database, create a super user
```bash
> python manage.py makemigrations
> python manage.py migrate
> python manage.py createsuperuser
> python manage.py runserver
```

## Testing

### Run tests:
```bash
python manage.py test
```

```bash
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..........
----------------------------------------------------------------------
Ran __ tests in _.___s

OK
Destroying test database for alias 'default'...
```

## Run on your Local machine

```bash
> python manage.py runserver
```
Then visit `http://localhost:8000` to view the app.
