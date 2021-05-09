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
python manage.py flush --no-input
python manage.py migrate

# Superuser Creation
script=$(cat << END
# If a super user exists
from django.contrib.auth import get_user_model

User = get_user_model()
User.objects.create_superuser('$SUPER_USER_MAIL', '$SUPER_USER_PASS')
END
)
        
echo "$script"| python manage.py shell
      
exec "$@"