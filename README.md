## ⚙️ ДЗ №3: Выгрузка сайта на хостинг
  
     http://studypythonrtk23.pythonanywhere.com/
    
     1. Обновить данные на хостинге git clone ......
  
  
  ## ⚙️ ДЗ №2: Коллеги, прошу строго не судить! Пересобрал новый проект, все, что успел сделать, залил) старй проект лежит тут https://github.com/Alex2421/DjangoNewsRostelecom

      1. Зарегистрируйте модель новости в панели администратора. -Сделал.  
      2.Настройте фильтры по различным полям: заголовок, дата создания,
      имя автора. - в работе! Фильтры сделаны, НО отключил, из-за них плывет меню, нет времени играться с версткой.
      3.Реализуйте функционал регистрации и авторизации пользователей  - Сделал.
      на отдельных страницах.
      4. Обеспечьте валидацию полей ввода данных на страницах регистрации и авторизации.  - Сделал.
      5) Обеспечьте привязку Автора новости к самой Новости (модели User
      из БД к записи новости - Article) при создании новости. - Вроде Сделал:)
      6) Создайте форму для поиска новости по заголовку, и отдельную
      страницу результатов поиска. Используйте механизмы аннотации и/или
      агрегации для получения сведений об Авторе новости в том же запросе к БД,
      что и запрос поиска новости по заголовку. - не успел!

  
  ## ⚙️ Проект был изменен:  ̶с̶а̶й̶т̶ ̶х̶о̶с̶т̶и̶н̶г̶о̶в̶о̶й̶ ̶к̶о̶м̶п̶а̶н̶и̶ / блог Python RTK:
  
  1. Проект лежит в директории /my_site
  2. Создан requirements.txt  - чтобы его использовать, запустите команду pip install -r requirements.txt
  3. пароль суперполльзователя admin/admin
  




## ⚙️ Установка и настройка проекта:

  1. Скопируйте репозиторий на ваше машину:
```bash
git clone https://github.com/..............
```
  2. Требуется создать и активировать виртуальную среду:
```bash
$ python3 -m venv venv
или создать ее в IDE

# Активация виртуальной среды в Windows:
$ source venv/Scripts/activate
         .venv/Scripts/activate 

# Активация виртуальной среды в Linux/Mac:
$ source venv/bin/activate
  source env/bin/activate
```
  3. Установка и создание requirements.txt пакета в python:
```bash
$ pip install -r requirements.txt
# создание requirements.txt
 pip freeze > requirements.txt
``` 
  4. Создание superuser :
```bash
$ python manage.py createsuperuser
```
```
#  Не создаеться superuser:  
Поставь в сеттингах вместо ru-ru en-en, после активации можно поменять.
ошибка: django.db.utils.OperationalError: no such table: auth_user
Решение - требуется сделать миграцию в БД ./manage.py migrate. После этого все запускается.
```  
 5. Запуск Django сервера:
```bash
$ python manage.py runserver
$ python manage.py makemigrations
$ python manage.py migrate
$ pip freeze | grep Django  - узнать версию установленного пакета
$ pip install django==4.2.8 - установка нужного пакета djangoсв 
$python manage.py migrate --fake MyApp zero - Сброс миграции отдельной таблицы
$python manage.py makemigrations

```
6. Установка Postgre:
   
$  windows https://www.postgresql.org/download/
+ настройки firewall netsh advfirewall firewall add rule name="Postgre Port" dir=in action=allow protocol=TCP localport=5432
