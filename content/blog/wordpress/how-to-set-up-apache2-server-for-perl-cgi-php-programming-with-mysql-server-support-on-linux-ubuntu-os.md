Title: How to set up Apache2 Server for PERL  CGI & PHP programming with MySQL Server support on Linux/Ubuntu OS
Date: 2017-11-11 19:37
Author: gauravssnl
Category: Linux, Networking, Ubuntu
Slug: how-to-set-up-apache2-server-for-perl-cgi-php-programming-with-mysql-server-support-on-linux-ubuntu-os
Status: published

Hello,everyone.Today,I want to share how we can set up **Apache2**  Server for PERL CGI and  PHP programming along with MySQL Server support on Linux/Ubuntu OS.

I am setting up **Apache2** Server on Ubuntu 16.04.You can do the same on your system easily by following my steps.

[[Steps:]{style="color:#ff00ff;text-decoration:underline;"}]{style="text-decoration:underline;"}

1.Install Apache2:\
[sudo apt install apache2]{style="color:#000000;"}

2.To start Apache2 server and test it (shown in screenshot):\
[sudo systemctl start apache2]{style="color:#000000;"}

To check status:\
[sudo systemctl status apache2]{style="color:#000000;"}

(Note: If you get any error in starting **Apache2** then **nginx**  or other server maybe running on system, so you can stop nginx by using this command: [sudo systemctl stop nginx]{style="color:#000000;"} ) and rerun the same command to start apache2.On my system, **nginx** starts automatically on reboot, so I have to stop it,otherwise apache2 server won't start.

![Screenshot from 2017-11-12 00-23-48.png](https://gauravssnl.files.wordpress.com/2017/11/screenshot-from-2017-11-12-00-23-48.png){.alignnone .size-full .wp-image-1868 width="1920" height="1080"}

 

if you see output as "[active (running)"]{style="color:#ff0000;"},then apache2 server is running successfully.Now,if you access  <http://localhost/>  in your browser, then you will see Apache2 Default Page.

\[Optional\]\
To stop Apache2 server:\
[sudo systemctl stop apache2]{style="color:#000000;"}\
To restart Apache2 server:\
[sudo systemctl restart apache2]{style="color:#000000;"}

 

2.Install Perl if it is not installed.\
[sudo apt install perl]{style="color:#000000;"}

3.To enable CGI for Apache2:\
[sudo a2enmod cgi]{style="color:#000000;"}\
[sudo systemctl restart apache2]{style="color:#000000;"}

4\. To write CGI files in /var/www/cgi-bin/ ,you need to use this command otherwise Apache2 will read CGI files from /usr/lib/cgi-bin/  :

[sudo vi /etc/apache2/sites-available/000-default.conf]{style="color:#000000;"}

This will open vi editor and lines will begin like this and we need to add the 3rd line given below(shown in screenshot) , and then save the file:

[ServerAdmin webmaster\@localhost]{style="color:#00ff00;"}\
[ DocumentRoot /var/www/html]{style="color:#00ff00;"}\
[ \# Add this 3rd line without editing other lines(you can ignore my other extra  lines  or use them if you want)]{style="color:#ff0000;"}\
[ScriptAlias /cgi-bin/ /var/www/cgi-bin/]{style="color:#000000;"}

![Screenshot from 2017-11-12 00-59-54](https://gauravssnl.files.wordpress.com/2017/11/screenshot-from-2017-11-12-00-59-54.png){.alignnone .size-full .wp-image-1930 width="1920" height="1080"}

 

5.Install MySQL if it is not installed (Remember MySQL password while installing as we need to use it later):\
[sudo apt-get install mysql-server]{style="color:#000000;"}

6.To run PERL programs which uses MySQL, you may need to install **DBI** & **DBD:mysql** for PERL by using these commands:\
[sudo cpan]{style="color:#000000;"}

Now **cpan** prompt will appear.Type these on prompt:\
[cpan\>]{style="color:#00ff00;"}[install DBI]{style="color:#000000;"}\
[capn\>]{style="color:#00ff00;"}[install DBD:mysq]{style="color:#000000;"}l

![Screenshot from 2017-11-06 16-59-12](https://gauravssnl.files.wordpress.com/2017/11/screenshot-from-2017-11-06-16-59-12.png){.alignnone .size-full .wp-image-1853 width="1920" height="1080"}

7.To start MySQL server:\
[sudo systemctl start mysql]{style="color:#000000;"}\
To check status of MySQL server:\
[sudo systemctl status mysql]{style="color:#000000;"}

![Screenshot from 2017-11-12 00-40-22.png](https://gauravssnl.files.wordpress.com/2017/11/screenshot-from-2017-11-12-00-40-22.png){.alignnone .size-full .wp-image-1906 width="1920" height="1080"}

if you see the output as ["active (running)"]{style="color:#ff0000;"} , then MySQL server is running successfully.

 

7.To use PHP with Apache2:\
[sudo apt install php libapache2-mod-php]{style="color:#000000;"}\
![Screenshot from 2017-11-06 20-29-54](https://gauravssnl.files.wordpress.com/2017/11/screenshot-from-2017-11-06-20-29-54.png){.alignnone .size-full .wp-image-1843 width="1920" height="1080"}

9.To enable PHP for apache2( change php7.0 with your version or just try 'php') :\
[sudo a2enmod php7.0]{style="color:#000000;"}

[sudo systemctl restart apache2]{style="color:#000000;"}

\# For PHP7.0\
[sudo apt install php7.0-mbstring]{style="color:#000000;"}

![Screenshot from 2017-11-06 20-30-00](https://gauravssnl.files.wordpress.com/2017/11/screenshot-from-2017-11-06-20-30-00.png){.alignnone .size-full .wp-image-1850 width="1920" height="1080"}

 

8.To enable PHP to connect with MySQL, use this command:\
[sudo apt install php-mysql]{style="color:#000000;"}

9.All the steps are complete now if all the previous steps are completed successfully .You need to place PERL CGI files in /var/www/cgi-bin/ directory so that you can access them in browser with URL http://localhost/cgi-bin/cgi.pl    .You need to write HTML and PHP files in /var/www/html directory so that you can acesss them in browser with URL http://localhost/index.html

Now, **Apache2 ** Server  is set up successfully for PERL CGI and PHP programming along with MySQL support on the system

Thanks for reading the post.I hope this post has been helpful and easy to understand.If you have any question or you face any error,please post it in comments.

 

 

 
