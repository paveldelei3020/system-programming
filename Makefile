# Переменные
NPM = npm
GIT = git

# Пример: make push m="описание фичи"
push:
	$(GIT) add .
	$(GIT) commit -m "$(m)"
	$(GIT) push
pull:
	$(GIT) pull

dev2:
	(cd ice_cream_4_forms && python manage.py runserver)