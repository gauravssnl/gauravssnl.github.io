Title: How to run and manage different versions of Python  with virtual environment support by using pyenv
Date: 2017-07-29 06:22
Author: gauravssnl
Category: Linux, Python, Ubuntu
Slug: how-to-run-and-manage-different-versions-of-python-with-virtual-environment-support-by-using-pyenv
Status: published

In this post,I am sharing how we can run different versions of python easily with virtual environment support  by usng **[pyenv]{style="color:#ff0000;"} .**I am using [**pyenv** ]{style="color:#ff0000;"}these days.I find it better than using [**virtualenv**]{style="color:#ff0000;"} .My currently activated environment remains activated even after restarting Terminal shell which I prefer.Another feature of [pyenv ]{style="color:#ff0000;"} is that you can set environment local to any folder.

Thanks : [Yamashita](https://github.com/yyuu)  (Author of [pyenv ]{style="color:#ff0000;"})

[Steps :]{style="color:#000000;"}

1.Use [[pyenv-installer](http://$%20curl%20-L%20https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer%20%7C%20bas)]{style="color:#ff0000;"}   to install pyenv.You can install pyenv by using this command on Terminal :

    $ curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash

 

2.To update  [pyenv]{style="color:#ff0000;"} ,use this command :

\$ pyenv update

![Screenshot from 2017-07-29 11-25-48.png](https://gauravssnl.files.wordpress.com/2017/07/screenshot-from-2017-07-29-11-25-48.png){.alignnone .size-full .wp-image-1763 width="1920" height="1080"}

 

3.Open your [**.bashrc**  ]{style="color:#ff0000;"}file and make sure that these lines are added to it .Otherwise,you need to add these lines  to your [**.bashrc** ]{style="color:#ff0000;"} file  by editing the file wih [sudo ]{style="color:#ff0000;"}command:

\# Load pyenv automatically by adding\
\# the following to \~/.bash_profile:

export PATH="/home/gaurav/.pyenv/bin:\$PATH"\
eval "\$(pyenv init -)"\
eval "\$(pyenv virtualenv-init -)"

 

4\. To install specific version of Python ,say Python 3.6.1 ,use this command :

\$ pyenv install 3.6.1

 

5.To create a virtual environment system ,say  [test]{style="color:#ff0000;"} which uses Python  3.6.1 which we installed in previous step,you can use this command :

\$ pyenv virtualenv 3.6.1 test

 

6.To activate this new virtual environment [test ]{style="color:#ff0000;"},you need to use this command :

\$ pyenv virtualenv 3.6.1 test

 

7.To list all virtual environments of pyenv ,use this command :

\$ pyenv versions

 

7.To switch back to system Python ,use this command :

\$ pyenv global system

 

![Screenshot from 2017-07-29 11-29-28.png](https://gauravssnl.files.wordpress.com/2017/07/screenshot-from-2017-07-29-11-29-28.png){.alignnone .size-full .wp-image-1780 width="1920" height="1080"}

 

8.To uninstall any virtual environment ,say [test ]{style="color:#ff0000;"},use this command and Entere[y ]{style="color:#ff0000;"} when it asks for confirmation :

\$ pyenv uninstall test

 

Now,you can easily run different versions of Python along with virtual environment support.

Thanks  for reading my post.I hope this post will be useful for them who  want to manage different versions of python with virtual environment support .If you have any query/question,please post in comments section.

 

 

 
