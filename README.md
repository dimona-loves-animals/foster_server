# Foster Server

## Initialize

### Database migration (at first run, or after updates)

locally:

    python manage.py migrate

(for this you must set the SECRET_KEY env var first)
    
or with docker:

    docker exec -it container_id python manage.py migrate

### Create super-admin user

(Note: locally is better used with virtual-env)

locally:

    python manage.py createsuperuser 

or with docker:

    docker exec -it container_id python manage.py createsuperuser

you can also use this:

    python manage.py createsuperuser --email admin@example.com --username admin

## Run server

### development notes

Make sure, before first run, to set the environment variables:

    DJANGO_SETTINGS_MODULE=foster_server.settings_dev
    SECRET_KEY=a-@$183+3zjsnf8c#bi0t!5rwqud!y3y(n5$pb%-1dm0@b4k!8

### production notes

Make sure, before first run, to set the environment variables:

    DJANGO_SETTINGS_MODULE=foster_server.settings_prod
    SECRET_KEY=a-@$183+3zjsnf8c#bi0t!5rwqud!y3y(n5$pb%-1dm0@b4k!8

> IMPORTANT!!!! update the SECRET_KEY to unique value!!!
    
or, if using docker:
 
create copy of the `docker-compose.production.yml` 
to `docker-compose.override.yml` which will set this up for you.

make an `.env` file from the `.env.example` file, and set the SECRET_KEY variable inside to unique value.

#### Test production settings

to test Production configuration use:

    docker-compose -f docker-compose.yml -f docker-compose.check.yml up

add `--build` if changes was made to the `settings.prod.py` file after first build

### run server

locally:

    python manage.py runserver 8080
    
or with docker:

    docker-compose up -d

## Development

Create new migration

    python manage.py makemigrations foster
    python manage.py sqlmigrate foster 0001

(for this you must set the SECRET_KEY env var first)