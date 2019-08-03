# django_NSR
 django
 =========================================================================================================================================
 
 CREATING PROJECT COMMANDS IN DJANGO:
 ------------------------------------------------------------------------------------------
 1.django-admin startproject 'projectname'
 2.python manage.py startapp 'appname'
 3.python manage.py makemigrations
 4.python manage.py migrate
 5.python manage.py runserver 'portnumber'
 
 
 
 
DJANGO WITH MYSQL CONNECTION (MYSQL COMMANDS DATABASE):
 ==========================================================================================================================================
 1.create datbase 'databasename';
 2.use 'databasename';
 3.show databases;
 4.show tables;
 5.select * from 'table name';
 6.truncate table 'tablename';
 7.drop database 'databasename'
  
   ===>verfiy connection with settings.py file database connection by using 'cursor()' function in python shell:
       ---------------------------------------------------------------------------------------------------------
       1.python manage.py shell
       2.from django.db import connection
       3.x=connection.cursor()

  

 DJANGO INSTALLATIONS:
 =========================================================================================================================================
 
 1.pip install django==1.9
 2.pip install pymysql
 3.pip install django-multiselectfield
 4.pip install pillow
 5.pip install djangorestframework
 
