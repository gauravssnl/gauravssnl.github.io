Title: How to set up Apache2 Server for PERL  CGI & PHP programming with MySQL Server support on Linux/Ubuntu OS
Date: 2017-11-11 19:37
Author: gauravssnl
Category: Linux, Networking, Ubuntu
Slug: how-to-set-up-apache2-server-for-perl-cgi-php-programming-with-mysql-server-support-on-linux-ubuntu-os
Status: published

Hello,everyone.Today,I want to share how we can set up **Apache2**  Server for PERL CGI and  PHP programming along with MySQL Server support on Linux/Ubuntu OS.

I am setting up **Apache2** Server on Ubuntu 16.04.You can do the same on your system easily by following my steps.

# Steps

1\. Install Apache2:
```bash
sudo apt install apache2
```

2\. To start Apache2 server and test it (shown in screenshot):
```bash
sudo systemctl start apache2
```

To check status:
```bash
sudo systemctl status apache2
```

(Note: If you get any error in starting **Apache2** then **nginx**  or other server maybe running on system, so you can stop nginx by using this command: [sudo systemctl stop nginx] ) and rerun the same command to start apache2.On my system, **nginx** starts automatically on reboot, so I have to stop it,otherwise apache2 server won't start.

![Screenshot from 2017-11-12 00-23-48.png](https://gauravssnl.files.wordpress.com/2017/11/screenshot-from-2017-11-12-00-23-48.png)

 

if you see output as "active (running)" ,then apache2 server is running successfully.Now,if you access  <http://localhost/>  in your browser, then you will see Apache2 Default Page.

**Optional**

To stop Apache2 server:
```bash
sudo systemctl stop apache2
```

To restart Apache2 server:
```bash
sudo systemctl restart apache2
```

3\. Install Perl if it is not installed.
```bash
sudo apt install perl
```

4\. To enable CGI for Apache2:
```bash
sudo a2enmod cgi
sudo systemctl restart apache2
```

5\. To write CGI files in **/var/www/cgi-bin/** ,you need to use this command otherwise Apache2 will read CGI files from **/usr/lib/cgi-bin/**  :
```bash
sudo vi /etc/apache2/sites-available/000-default.conf
```
This will open vi editor and lines will begin like this and we need to add the 3rd line given below(shown in screenshot) , and then save the file:
```code
ServerAdmin webmaster\@localhost]
DocumentRoot /var/www/html
# Add this 3rd line without editing other lines(you can ignore my other extra  lines  or use them if you want
ScriptAlias /cgi-bin/ /var/www/cgi-bin/
```

![Screenshot from 2017-11-12 00-59-54](https://gauravssnl.files.wordpress.com/2017/11/screenshot-from-2017-11-12-00-59-54.png)

 

6\.Install MySQL if it is not installed (Remember MySQL password while installing as we need to use it later):
```bash
sudo apt-get install mysql-server
```

7\.To run PERL programs which uses MySQL, you may need to install **DBI** & **DBD:mysql** for PERL by using these commands:
```bash
sudo cpan
```
Now **cpan** prompt will appear.Type these on prompt:
```shell
cpan\> install DBI
cpan\> install DBD:mysql
```

![Screenshot from 2017-11-06 16-59-12](https://gauravssnl.files.wordpress.com/2017/11/screenshot-from-2017-11-06-16-59-12.png)

8.To start MySQL server:
```bash
sudo systemctl start mysql
```
To check status of MySQL server:
```bash
sudo systemctl status mysql
```
![Screenshot from 2017-11-12 00-40-22.png](https://gauravssnl.files.wordpress.com/2017/11/screenshot-from-2017-11-12-00-40-22.png)

if you see the output as "active (running)" , then MySQL server is running successfully.


9\. To use PHP with Apache2:
```bash
sudo apt install php libapache2-mod-php
```
![Screenshot from 2017-11-06 20-29-54](https://gauravssnl.files.wordpress.com/2017/11/screenshot-from-2017-11-06-20-29-54.png)

10\. To enable PHP for apache2( change php7.0 with your version or just try 'php') :
```bash
sudo a2enmod php7.0
sudo systemctl restart apache2
```

\# For PHP7.0
```bash
sudo apt install php7.0-mbstring
```

![Screenshot from 2017-11-06 20-30-00](https://gauravssnl.files.wordpress.com/2017/11/screenshot-from-2017-11-06-20-30-00.png)

 
11\. To enable PHP to connect with MySQL, use this command:
```bash
sudo apt install php-mysql
```

12\. All the steps are complete now if all the previous steps are completed successfully .You need to place PERL CGI files in /var/www/cgi-bin/ directory so that you can access them in browser with URL http://localhost/cgi-bin/cgi.pl   .You need to write HTML and PHP files in /var/www/html directory so that you can acesss them in browser with URL http://localhost/index.html

Now, **Apache2** Server  is set up successfully for PERL CGI and PHP programming along with MySQL support on the system

Thanks for reading the post.I hope this post has been helpful and easy to understand.If you have any question or you face any error,please post it in comments.

 

 

 
