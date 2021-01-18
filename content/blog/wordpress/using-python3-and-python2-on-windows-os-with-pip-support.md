Title: Using Python3 and Python2 on Windows OS with pip support
Date: 2017-05-06 15:00
Author: gauravssnl
Category: Python, Windows
Slug: using-python3-and-python2-on-windows-os-with-pip-support
Status: published

Hello everyone.Today,I am going to share how to use Python3 and Python2 with pip support  on Windows OS.If you try to install latest Python version 3.6 ,it provides you the option of adding Python 3.6 to PATH ,but this is not provided by Python2 installer still.Many users may find it difficult to use both version with corresponding pip on Windows OS.

So,I am sharing this method which helped me to use Python2 and Python3 simultaneously.

# STEPS

1.Download **Python3** and **Python2** installer from [python.org](http://python.org) .

2.Run **Python3** installer and tick(enable) *"Add Python 3.6 to Path"* as shown in screenshot so that you can run Python3 by `python` command on Terminal/Shell.

![p3s](https://gauravssnl.files.wordpress.com/2017/05/p3s.jpg)


3.You can run Python3 by using `python` command and its pip by using `pip` command.

4.Run Python2 installer and install Python2 .

5.Now ,you need to edit system environment  variable `PATH` as shown in screenshot below  for using Python2  and its **pip2** in Terminal/shell :

![path_setup](https://gauravssnl.files.wordpress.com/2017/05/path_setup.jpg)



6.Click on Edit Button .After that all the enteries of `PATH` variable will be displayed.Now,click on New Button and add this entry as shown in screenshot:

`C:\\Python27\\Scripts`

![path_edit.JPG](https://gauravssnl.files.wordpress.com/2017/05/path_edit.jpg)
 

7.Click on OK button to save and make it sure that the entry added to `PATH` varaiable is not `C:\\Python27`. Otherwise, `python` command will run Python2 instead of Python3 .

8\. Again add a new entery `PY_PATH` to system variables and set its value to 2 if you want to run python2 by using `py` command.

9.Now, you can use Python 3 by using `python` or `py -3`. You can use pip for python 3 by `pip` or `pip3` command .You can use Python2 by using `py` command or `py-2 `command .You can use pip for Python2 by using `pip2` command.(*See Screenshot)*

![pipnnn.JPG](https://gauravssnl.files.wordpress.com/2017/05/pipnnn.jpg)

 

If every step is followed correctly,you will see Python3 and Python2 running successfully with pip support in Terminal.

If you have any query or you need help,post in comments.I will be glad to help you.

Thanks for reading my post.I hope my post will be useful to Python users who are using **Windows** OS.

 

 

 
