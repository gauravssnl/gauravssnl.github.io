Title: How to run and manage different versions of Python  with virtual environment support by using pyenv
Date: 2017-07-29 06:22
Author: gauravssnl
Category: Linux, Python, Ubuntu
Slug: how-to-run-and-manage-different-versions-of-python-with-virtual-environment-support-by-using-pyenv
Status: published

In this post,I am sharing how we can run different versions of python easily with virtual environment support  by usng **[pyenv]**.I am using **pyenv** these days.I find it better than using **virtualenv**. My currently activated environment remains activated even after restarting Terminal shell which I prefer. Another feature of **pyenv** is that you can set environment local to any folder.

Thanks : [Yamashita](https://github.com/yyuu)  (Author of **pyenv**)

# Steps 

1\. Use [pyenv-installer](http://$%20curl%20-L%20https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer%20%7C%20bas)] to install pyenv.You can install pyenv by using this command on Terminal :
```console
$ curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
```
 

2\. To update **pyenv** ,use this command :
```console
$ pyenv update
```
![Screenshot from 2017-07-29 11-25-48.png](https://gauravssnl.files.wordpress.com/2017/07/screenshot-from-2017-07-29-11-25-48.png)


3\. Open your **.bashrc** file and make sure that these lines are added to it .Otherwise,you need to add these lines  to your **.bashrc** file  by editing the file wih **sudo** command:
```script
# Load pyenv automatically by adding
# the following to ~/.bash_profile:

export PATH="/home/gaurav/.pyenv/bin:\$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

4\. To install specific version of Python ,say Python 3.6.1 ,use this command :
```bash
$ pyenv install 3.6.1
```
 

5\. To create a virtual environment system ,say  **test** which uses Python  3.6.1 which we installed in previous step,you can use this command :
```bash
$ pyenv virtualenv 3.6.1 test
```

6\. To activate this new virtual environment **test**,you need to use this command :
```bash
$ pyenv virtualenv 3.6.1 test
```

7\. To list all virtual environments of pyenv ,use this command :
```bash
$ pyenv versions
```

8\. To switch back to system Python ,use this command :
```bash
$ pyenv global system
```
![Screenshot from 2017-07-29 11-29-28.png](https://gauravssnl.files.wordpress.com/2017/07/screenshot-from-2017-07-29-11-29-28.png)

9\. To uninstall any virtual environment ,say **test**,use this command and Entere **y** when it asks for confirmation :
```bash
$ pyenv uninstall test
```

Now,you can easily run different versions of Python along with virtual environment support.

Thanks  for reading my post.I hope this post will be useful for them who  want to manage different versions of python with virtual environment support .If you have any query/question,please post in comments section.

 

 

 
