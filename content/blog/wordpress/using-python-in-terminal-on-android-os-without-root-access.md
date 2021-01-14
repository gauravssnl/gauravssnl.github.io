Title: Using Python in Terminal on Android OS  without Root Access
Date: 2016-09-03 19:48
Author: gauravssnl
Category: Android, Python
Slug: using-python-in-terminal-on-android-os-without-root-access
Status: published

Hello,everyone.Today,I am going to share how to use Python in Terminal on Android phone without Root Access.This post is made for them who do not use Rooted phone or those who do not want to Root.

I had thought that it would not be possible to use Python in Terminal without Root Access.Python scripts can also be run using Sl4A , but I find using Python in Terminal better as Sl4a has no option of changing directory.Running Python files is easier in Terminal.So,let us proceed to the tutorial.

**Tools Required: **

1\. Python For Android.apk: [Download Here](http://upfile.mobi/bMOYKSKTeaq)

2.Terminal.apk :  [Download Here](http://upfile.mobi/aDy0JAy4SOc)

3\. Python.sh: [Download Here](http://upfile.mobi/JViKQsoVoo7)

4\. Sl4A.apk(optional file):[ Download Here](http://upfile.mobi/1OyKFOLxHe3) \
**Steps: **

1.Download all of the above files if you do not have.Install Python For Android app. You can also install Sl4A app if you want.

2.Open Python For Android app and click on Install button to install Python library on your phone .Internet is required for first time installation.After successful installation of Python library,your screen should be like as shown in screenshot given below:

[![](http://gauravssnl.files.wordpress.com/2016/09/screenshot_2016-09-03-19-28-48.png){.wp-image-905 .alignnone .size-full width="720" height="1280"}](http://gauravssnl.files.wordpress.com/2016/09/screenshot_2016-09-03-19-28-48.png)

3.Now,copy **Python.sh** file to your internal memory **sdcard  **as shown in the screenshot.

[![](http://gauravssnl.files.wordpress.com/2016/09/screenshot_2016-09-03-14-09-17.png){.wp-image-907 .alignnone .size-full width="720" height="1280"}](http://gauravssnl.files.wordpress.com/2016/09/screenshot_2016-09-03-14-09-17.png)

3.Now,open Terminal app.To run Python,type these carefully as shown in screenshot:

**sh  **/**sdcard/python.sh **

[![](http://gauravssnl.files.wordpress.com/2016/09/screenshot_2016-09-04-00-55-46.png){.wp-image-908 .alignnone .size-full width="720" height="1280"}](http://gauravssnl.files.wordpress.com/2016/09/screenshot_2016-09-04-00-55-46.png)

4.If everything is fine,you will see Python successfully running on Terminal.If,you get error as Python.sh file not found,make sure that **python.sh** is there in internal sdcard(**/sdcard** ).

5.To run a script file say **hello.py** of folder **scripts** in your sdcard(**/sdcard/scripts folder)** as shown in screenshot:

[![](http://gauravssnl.files.wordpress.com/2016/09/screenshot_2016-09-03-14-41-351.png){.wp-image-909 .alignnone .size-full width="720" height="1280"}](http://gauravssnl.files.wordpress.com/2016/09/screenshot_2016-09-03-14-41-351.png)we need to type the following command carefully to run hello.py file( **/**sdcard**/**scripts**/**hello**.**py ) as shown in screenshot below :

**cd /sdcard/scripts**

**sh  /sdcard/python.sh   hello.py**

[![](http://gauravssnl.files.wordpress.com/2016/09/screenshot_2016-09-03-14-41-07.png){.wp-image-910 .alignnone .size-full width="720" height="1280"}](http://gauravssnl.files.wordpress.com/2016/09/screenshot_2016-09-03-14-41-07.png)

6\. In this way you can run any Python file present in current directory on Terminal app by using the following command:

sh  /sdcard/Python.sh  filename.py

Now,you can use Python and Python Scripts on all  Android OS without Root Access in the way shown above.Tutorial is complete now.

I hope this tutorial will be useful for many users.Thanks everyone for reading my post.

If you have any questions or you get any error,please contact me by posting your comments.

Share this if you really like it.

©gauravssnl
