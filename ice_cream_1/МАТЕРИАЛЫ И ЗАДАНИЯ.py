urlpatterns = [
    path('page/', views.maks_karpov),    
    path('page/', views.alan_turing),
] 





urlpatterns = [
    path('page/<int:pk>/', views.maks_karpov),    
    path('page/1/', views.alan_turing),
] 







# 1 вопрос
# В списке urlpatterns Django-проекта задан единственный шаблон:

# Файл urls.py

...
urlpatterns = [
    path('hamsters/<slug:category>/', views.strange_hamsters_list),
] 



# При запросе к какому URL будет вызвана функция strange_hamsters_list()?


# 1.  /hamsters/flying/
# 2.  /hamsters/
# 3.  /dancing/hamsters/
# 4.  /hamsters/lets_dance/
# 5.  /hamsters/sing.sing.sing/




# Вопрос 2
# Список адресов в проекте теперь выглядит так:

...
urlpatterns = [
    path('admin/<int:pk>/', views.admin_detail),
    path('<slug:category_slug>/', views.item_category),
    path('admin/', views.admin),
] 
# Пользователь отправил запрос на URL /admin/. Какая view-функция будет вызвана:

# 1.Функция admin_detail() из файла views.py.
# 2.Функция admin() из файла views.py.
# 3.Функция item_category() из файла views.py.




# Вопрос 3
...
urlpatterns = [
    path('<slug:category>/', views.product_category_slug),
    path('<str:category>/', views.product_category_str),
    path('<int:category>/', views.product_category_int),
] 

# При каком из запросов будет вызвана view-функция product_category_int()?
# 1. /утюг/
# 2. /152/
# 3. /iron/
# 4. Ни один из перечисленных запросов не будет обработан функцией product_category_int().











# ЗАДАНИЕ 1
# Настройте корневой файл anfisa_for_friends/urls.py и файл homepage/urls.py так,
# чтобы запрос к главной странице обрабатывался view-функцией index() из приложения homepage.




# ЗАДАНИЕ 2
# Попробуйте открыть страницу about/. Для этого в открывшейся вкладке браузера к
# адресу страницы добавьте путь about/ и перейдите по нему. Проект вернёт страницу ошибки:
# ведь адрес about/ не подключён к маршрутизатору.

# Настройте маршрутизатор так, чтобы страница about/ обрабатывалась view-функцией description() из приложения about. 

# Для этого нужно:
# создать в приложении about файл urls.py,
# импортировать в этот файл функцию path() и файл views.py,
# объявить список urlpatterns и добавить в него один элемент: path(маршрут, view_функция),
# в корневом urls.py добавить path(), который подключит пути из файла about/urls.py для обработки запроса about/.


# После выполнения работы обновите страницу about/, открытую в браузере.
# Если всё сделано правильно — вместо страницы с ошибкой будет отображена страница,
# созданная view-функцией description() из about/views.py.




# ЗАДАНИЕ 3
# Настройте корневой urls.py:
# все адреса вида ice_cream/... должны передаваться в urls.py приложения ice_cream;
# Создайте файл urls.py в приложении ice_cream. В нём настройте адреса таким образом, чтобы:
# запросы к адресу ice_cream/ обрабатывались view-функцией ice_cream_list() из приложения ice_cream;

# запросы к адресам вида ice_cream/1/, ice_cream/2/, ice_cream/42/
# и к прочим подобным — view-функцией ice_cream_detail() из приложения ice_cream.
# В качестве переменной пути должны приниматься только положительные целочисленные значения и ноль.



# ЗАДАНИЕ 4
# Допишите view-функции в приложениях homepage, about и ice_cream так,
# чтобы при запросах к проекту в браузере выводился текст в зависимости от запрошенного URL:

# Относительный адрес	Текст
''	                'Главная страница'
'about/'	        'Описание проекта'
'ice_cream/'	    'Каталог мороженого'
'ice_cream/1/'	    'Мороженое номер 1'
'ice_cream/2/'	    'Мороженое номер 2'
...	...
'ice_cream/100500/'	'Мороженое номер 100500'

# Оборачивать текст в HTML-теги необязательно.