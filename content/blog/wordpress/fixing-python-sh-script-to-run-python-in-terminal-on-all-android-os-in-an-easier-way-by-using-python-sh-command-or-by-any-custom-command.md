Title: Fixing python.sh script to run Python in Terminal on all Android OS in an easier way by using  python.sh command or by any custom command
Date: 2016-09-05 15:33
Author: gauravssnl
Category: Uncategorized
Slug: fixing-python-sh-script-to-run-python-in-terminal-on-all-android-os-in-an-easier-way-by-using-python-sh-command-or-by-any-custom-command
Status: published

Hello,everyone.Today, I am going to share how to fix my old **python**.**sh** script which I had shared on my blog for using Python in Terminal and how to use **python.sh** command** **after fixing that.

At first,I would like to thank my friend **Luiz** who fixed the old python.sh script which I had shared with you all on this blog.

I consider that [Python For Android](http://upfile.mobi/bMOYKSKTeaq)  app and its Python library has been already installed by you.If,you are using my old **python.sh** script  which you have already copied to **/system/bin** ,set its permission as **777**,and try to run Python in Terminal  with this command: **python.sh  **,you will get error as shown in the screenshot:

[![](http://gauravssnl.files.wordpress.com/2016/09/screenshot_2016-09-05-11-13-01.png){.wp-image-915 .alignnone .size-full width="720" height="1280"}](http://gauravssnl.files.wordpress.com/2016/09/screenshot_2016-09-05-11-13-01.png)This error is shown due to an error in first line of python.sh script as shown in screenshot:

**\#! /bin/sh **

[![](http://gauravssnl.files.wordpress.com/2016/09/screenshot_2016-09-05-11-13-33.png){.wp-image-916 .alignnone .size-full width="720" height="1280"}](http://gauravssnl.files.wordpress.com/2016/09/screenshot_2016-09-05-11-13-33.png)

You are able to use Python only by using this command which is long and complex to type:

**sh /system/bin/python.sh**

***\
***

***\*Fixing python.sh  file:***

Android executes commands from **/system/bin** or **/system/xbin** .So,we need to edit the first line of ** python.sh** script of **/system/bin  **directory as shown below in screenshot:

**\# !/system/bin/sh **

[![](http://gauravssnl.files.wordpress.com/2016/09/img_20160905_153322.jpg){.wp-image-917 .alignnone .size-full width="720" height="1280"}](http://gauravssnl.files.wordpress.com/2016/09/img_20160905_153322.jpg)

Save the file and check that it's permission is assigned as 777.

Or,you can download my  fixed **python.sh** file from below.

Download Here: [python.sh](http://upfile.mobi/Hw2pJ62c4GY)

Now,open Terminal app and use this simple command to run Python  as shown in screenshot:

**python.sh**

[![](http://gauravssnl.files.wordpress.com/2016/09/screenshot_2016-09-05-11-15-01.png){.wp-image-918 .alignnone .size-full width="720" height="1280"}](http://gauravssnl.files.wordpress.com/2016/09/screenshot_2016-09-05-11-15-01.png)**\
**

You can see Python running successfully on your Terminal.If you get any error,there might be some mistakes.You need to check your all steps carefully.T o run any file in current directory,you need to use this command:

**python.sh filename.py**

**\
**

**\*Customising(Renaming) python.sh command to any desired name **

You can also rename **python.sh** file of **/system/bin** directory to whatever name you like . you need to remember that name and use that name as command to run Python.For example,I have renamed **python**.**sh** to **gaurav** as shown in screenshot:

[![](http://gauravssnl.files.wordpress.com/2016/09/screenshot_2016-09-05-11-16-58.png){.wp-image-919 .alignnone .size-full width="720" height="1280"}](http://gauravssnl.files.wordpress.com/2016/09/screenshot_2016-09-05-11-16-58.png)

Now,open Terminal app,and use the command **gaurav** (you use the name whatever you have given to **python.sh** file) ,you will see Python successfully running with your customised command as shown in screenshot:

[![](http://gauravssnl.files.wordpress.com/2016/09/screenshot_2016-09-05-11-18-00.png){.wp-image-920 .alignnone .size-full width="720" height="1280"}](http://gauravssnl.files.wordpress.com/2016/09/screenshot_2016-09-05-11-18-00.png)

You will see Python running successfully if everything is fine.Now,You have successfullychanged/customised python.sh command.You need to use that command every time to run Python.

Thanks everyone for reading this post.If you have any questions or you get any error,please post in Comments.
