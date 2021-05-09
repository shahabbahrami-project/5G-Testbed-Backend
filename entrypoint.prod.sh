#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Migration
python manage.py migrate --no-input

# Static files
python manage.py collectstatic --no-input --clear

# Superuser Creation
script=$(cat << END
# If a super user exists
from django.contrib.auth import get_user_model

User = get_user_model()

if User.objects.filter(email='$SUPER_USER_MAIL').count()==0:
  User.objects.create_superuser('$SUPER_USER_MAIL', '$SUPER_USER_PASS')
else:
  print('A Super user with same email exist!')
END
)
        
echo "$script"| python manage.py shell

exec "$@"