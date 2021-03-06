**Windows:**
https://www.codementor.io/@aswinmurugesh/deploying-a-django-application-in-windows-with-apache-and-mod_wsgi-uhl2xq09e
***make sure your python and apache installation files are all 64 bit or 32***
1. Install Python
    - Make sure both the checboxes at the bottom of the window are checked (Install for all users, and Add Python 3.7 to PATH checkboxes)

2. Download Visual Studio 2017 from https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads. When installing Visual Studio, make sure you select Desktop Environment with C++ on Workloads section, and the C++/CLI Support option on the right side of the screen.

3. Download the latest Visual C++ from https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads and install it

4.  Download the latest version of MySQL from https://dev.mysql.com/downloads/mysql/. Run the downloaded setup file
    - In the type of installation, choose Developer Default
    - In the Type and Networking page, choose Config Type as Server Computer
    -  setup the root user's password. And in the users section, add a user with the name as same as the logged in user

5. Create DB and previlage
mysql> create database my_application;
Query OK, 1 row affected (0.04 sec)

mysql> grant all on my_application.* to '<my-user>'@'localhost';
Query OK, 0 rows affected (0.08 sec)

6. On CMD

pip install virtualenvwrapper-win

mkvirtualenv my_application

workon my_application

pip install django

pip install pymysql

python manage.py makemigrations

python manage.py migrate

python manage.py collectstatic

7. Download WAMP server from http://www.wampserver.com/en/#download-wrapper. The default installation should have created a folder in C:, as C:\wamp64

8. add an Environment variable in your machine with name MOD_WSGI_APACHE_ROOTDIR whose value should be C:\wamp64\bin\apache\apache<version>\.

9. pip install mod_wsgi

10. mod_wsgi-express module-config

    - The output should be something similar to:
    LoadFile "c:/users/myuser/appdata/local/programs/python/python37/python37.dll"
LoadModule wsgi_module "c:/users/myuser/appdata/local/programs/python/python37/lib/site-packages/mod_wsgi/serve
r/mod_wsgi.cp37-win_amd64.pyd"
WSGIPythonHome "c:/users/myuser/appdata/local/programs/python/python37"

11. Copy the output generated by the mod_wsgi-express command and paste it at the end of C:\wamp64\bin\apache\apache<version>\conf\httpd.conf.

12. open the vhosts file at C:\wamp64\bin\apache\apache<version>\conf\extra\httpd_vhosts.conf and replace the contents over there with the content below:

    # virtual SupervisionTool
    <VirtualHost *:80>
        ServerName localhost 
        WSGIPassAuthorization On
        ErrorLog "logs/my_application.error.log"
        CustomLog "logs/my_application.access.log" combined
        WSGIScriptAlias /  "C:\Users\myuser\my_application\my_application\wsgi_windows.py"
        <Directory "C:\Users\myuser\my_application\my_application">
            <Files wsgi_windows.py>
                Require all granted
            </Files>
        </Directory>

        Alias /static "C:/Users/myuser/my_application/static"
        <Directory "C:/Users/myuser/my_application/static">
            Require all granted
        </Directory>  
    </VirtualHost>
    # end virtual SupervisionTool

13. you should now be able to go to the System Services panel, start the Apache service and you should be able to access the application at http://localhost

