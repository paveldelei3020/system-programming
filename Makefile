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

dev1:
	(cd ice_cream && python manage.py runserver)

dev2:
	(cd ice_cream_1 && python manage.py runserver)