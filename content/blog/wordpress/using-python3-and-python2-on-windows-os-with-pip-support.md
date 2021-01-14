Title: Using Python3 and Python2 on Windows OS with pip support
Date: 2017-05-06 15:00
Author: gauravssnl
Category: Python, Windows
Slug: using-python3-and-python2-on-windows-os-with-pip-support
Status: published

Hello everyone.Today,I am going to share how to use Python3 and Python2 with pip support  on Windows OS.If you try to install latest Python version 3.6 ,it provides you the option of adding Python 3.6 to PATH ,but this is not provided by Python2 installer still.Many users may find it difficult to use both version with corresponding pip on Windows OS.

So,I am sharing this method which helped me to use Python2 and Python3 simultaneously.

**[STEPS]{style="color:#800080;"} :**

1.Download P**ython3 **and **Python2 **installer from [python.org](http://python.org) .

2.Run **Python3 **installer and tick(enable) "[*Add Python 3.6 to Path[" as shown in screenshot so that you can run Python3 by [python ]{style="color:#ff0000;"}command on Terminal/Shell.]{style="color:#333333;"}*]{style="color:#ff0000;"}

![p3s](https://gauravssnl.files.wordpress.com/2017/05/p3s.jpg){.alignnone .size-full .wp-image-1352 width="1009" height="623"}

 

3.You can run Python3 by using [python ]{style="color:#ff0000;"}command and its pip by using [pip ]{style="color:#ff0000;"}command.

4.Run Python2 installer and install Python2 .

5.Now ,you need to edit system environment  variable [PATH]{style="color:#ff0000;"} as shown in screenshot below  for using Python2  and its **pip2** in Terminal/shell :

![path_setup](https://gauravssnl.files.wordpress.com/2017/05/path_setup.jpg){.alignnone .size-full .wp-image-1362 width="892" height="968"}

 

6.Click on Edit Button .After that all the enteries of [ PATH  ]{style="color:#ff0000;"}variable will be displayed.Now,click on New Button and add this entry as shown in screenshot:

**C:\\Python27\\Scripts**

[![path_edit.JPG](https://gauravssnl.files.wordpress.com/2017/05/path_edit.jpg){.alignnone .size-full .wp-image-1371 width="1632" height="836"}]{style="color:#000000;"}

 

7.Click on OK button to save and make it sure that the entry added to [PATH ]{style="color:#ff0000;"}varaiable is not **[C:\\Python27[\\ ]{style="color:#000000;"}]{style="color:#000000;"}**[ ]{style="color:#000000;"} . [Otherwise , [python [command will run Python2 ]{style="color:#000000;"}]{style="color:#ff0000;"}instead of Python3 .]{style="color:#000000;"}

8\. Again add a new entery [PY_PATH ]{style="color:#ff0000;"}to system variables and set its value to 2 if you want to run python2 by using [py ]{style="color:#ff0000;"}command.

9.Now, you can use Python 3 by using [python [or [py -3]{style="color:#ff0000;"}]{style="color:#000000;"} ]{style="color:#ff0000;"}. You can use pip for python 3 by [pip ]{style="color:#ff0000;"}or [pip3 ]{style="color:#ff0000;"}command .You can use Python2 by using [py [command or [py-2 ]{style="color:#ff0000;"}command .]{style="color:#000000;"}]{style="color:#ff0000;"}You can use pip for Python2 by using [pip2 ]{style="color:#ff0000;"}command.(*See Screenshot)*

![pipnnn.JPG](https://gauravssnl.files.wordpress.com/2017/05/pipnnn.jpg){.alignnone .size-full .wp-image-1437 width="1920" height="1080"}

 

If every step is followed correctly,you will see Python3 and Python2 running successfully with pip support in Terminal.

If you have any query or you need help,post in comments.I will be glad to help you.

Thanks for reading my post.I hope my post will be useful to Python users who are using **Windows** OS.

 

 

 
