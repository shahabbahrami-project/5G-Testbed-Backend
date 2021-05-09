# recipe-app-api
Recipe app api source code.

**Running Development Container**

Create the the following files in **root** directory:
- **.env.dev** should contain the following values:
		DEBUG
		SECRET_KEY
		DJANGO_ALLOWED_HOSTS
		SUPER_USER_MAIL
		SUPER_USER_PASS
- **.env.dev.db** should contain the following values:
		POSTGRES_DB
		POSTGRES_USER
		POSTGRES_PASSWORD
		SQL_ENGINE
		SQL_HOST
		SQL_PORT
Build:
		docker-compose up -d --build
*You can access website on http://127.0.0.1:1337/*

**Running Production Container**

Create the the following files in **root** directory:
- **.env.prod** should contain the following values:
		DEBUG
		SECRET_KEY
		DJANGO_ALLOWED_HOSTS
		SUPER_USER_MAIL
		SUPER_USER_PASS

- **.env.prod.db** should contain the following values:
		POSTGRES_DB
		POSTGRES_USER
		POSTGRES_PASSWORD
		SQL_ENGINE
		SQL_HOST
		SQL_PORT
Build:
		docker-compose -f docker-compose.prod.yml up -d --build
*You can access website on http://0.0.0.0:8005/*
--Ali