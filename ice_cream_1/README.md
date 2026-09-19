Ознакомьтемь с проектом, установите виртуальное окружение и джанго. 
Рекомендуется использовать python 3.9 и django 3.2
Затем примените миграции и запустите сервер.



python -m venv venv            (win)     python3 -m venv venv      (linux/MacOS)

source venv/Scripts/activate   (win)     source venv/bin/activate  (linux/MacOS)

pip install Django==3.2

python manage.py migrate                    Применить миграции  (Применение созданных миграций или "пуш" для БД)

python manage.py makemigrations             Сделать миграции    (черновик/чертеж/"коммит" для БД)

python manage.py runserver
