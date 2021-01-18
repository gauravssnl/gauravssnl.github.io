Title: Easy way of Using Python v2.7 in Android Terminal by GAE Proxy Application Method
Date: 2016-08-13 07:26
Author: gauravssnl
Category: Android, Python
Slug: easy-way-of-using-python-v2-7-in-android-terminal-by-gae-proxy-application-method
Status: published

Good Aftetnoon Friends.Today I would like to share how to use Python v2.7 in Android Terminal.Many have been finding it difficult to use Python in Terminal.This is old and easy trick. So,let us begin.

Note: Your Android phone must be rooted.If you do not know about Rooting,Search on Google.

**Tools Required:**

1.  Terminal application: [Download Here](http://upfile.mobi/aDy0JAy4SOc)
2.  GAE(Google App Engine) Proxy application: [Download Here](http://upfile.mobi/L97xQWCXP7C)

**Steps:**

-   Download all of the above applications and install them.Open GAE Proxy & exit it.
-   Now go to `/data/data/org.gaeproxy` folder,you will see `python-cl` file.Select it & copy it to `/system/bin` folder (see screenshot).

[![](http://gauravssnl.files.wordpress.com/2016/08/screenshot_2016-08-13-12-27-012.png){.wp-image-674 .alignnone .size-full width="720" height="1280"}](http://gauravssnl.files.wordpress.com/2016/08/screenshot_2016-08-13-12-27-012.png)

[![](http://gauravssnl.files.wordpress.com/2016/08/screenshot_2016-08-13-12-26-26.png){.wp-image-675 .alignnone .size-full width="720" height="1280"}](http://gauravssnl.files.wordpress.com/2016/08/screenshot_2016-08-13-12-26-26.png)

.Rename `python-cl` file in `/system/bin` folder to whatever name you want but you need to remember the name you give.I have changed `python-cl` file of `/system/bin` to `gaurav`. This name will be used to run python on terminal(see screenshot)

[![](http://gauravssnl.files.wordpress.com/2016/08/screenshot_2016-08-13-12-40-32.png){.wp-image-676 .alignnone .size-full width="720" height="1280"}](http://gauravssnl.files.wordpress.com/2016/08/screenshot_2016-08-13-12-40-32.png)

- Now open terminal .Type this on terminal(see screenshot):
```bash
su
gaurav
```

[![](http://gauravssnl.files.wordpress.com/2016/08/screenshot_2016-08-13-12-43-32.png){.wp-image-677 .alignnone .size-full width="720" height="1280"}](http://gauravssnl.files.wordpress.com/2016/08/screenshot_2016-08-13-12-43-32.png)

- Now you will see python 2.7 running successfully in Terminal
-   To run any file `abc.py`, type this in terminal:
```bash
gaurav abc.py
``` 

Note: Execute `su` command always first,then only you can use `gaurav` command in Terminal to run Python.

I hope this tutorial will be helpful for them who are new to using Python on Android in Terminal.

Thanks to Kang Aswan Suryadinata for this method.Thanks to my friends,family and facebook group where I learn so many things.

If you have any questions, please post in comments.Happy Phreaking.

©gauravssnl
