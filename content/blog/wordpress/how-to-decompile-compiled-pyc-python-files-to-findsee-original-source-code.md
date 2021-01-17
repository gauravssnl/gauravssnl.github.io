Title: How to decompile compiled .pyc python files to find/see original source code
Date: 2017-07-01 09:03
Author: gauravssnl
Category: Decompiling, Python, Reverse Engineering, Ubuntu, Windows
Slug: how-to-decompile-compiled-pyc-python-files-to-findsee-original-source-code
Status: published

Hello, everyone. In this post,i am sharing how to decompile compiled python files which are in .pyc formats usually. It may be useful for reverse enginering and if you want to know the original source code of any compiled python files. It may be also useful whenever  your original .py  python file is deleted unknowingly and there is only compiled .pyc file left  on disk and you want your original .py file back. In all those cases, this method can be used.

I have used Ubuntu OS here and it can be used on Windows OS also.

# Tools Required 

**uncompyle6** <https://github.com/rocky/python-uncompyle6/>

Thanks : *R. Bernstein* (Author of uncompyle6)

# Steps

1\. Install **uncompyle6** by using **pip** on Terminal or you can download from above link and install it by running its **setup.py** file. To install **uncompyle6** by using **pip**, use this command on Terminal :
```bash
pip install uncompyle6
```

2\. After installation of **uncompyle6**,you can check its successfull installation and its usage by running  **uncompyle6** command on Terminal (see screenshot).


3\. To decompile any file in current diectory ,use command (see screenshot for example): 
`uncompyle6 -o . <file-name.pc> `

Example : `uncompyle6 -o . txfile.pyc rxfile.pyc`

![Screenshot from 2017-07-01 13-38-05](https://gauravssnl.files.wordpress.com/2017/07/screenshot-from-2017-07-01-13-38-05.png)

4\. You will see your decompiled files created with same name in the current working directory(or desired directory) .Now,you can open this decompiled file with any Text Editor and see original source code.

![Screenshot from 2017-07-01 13-38-46.png](https://gauravssnl.files.wordpress.com/2017/07/screenshot-from-2017-07-01-13-38-46.png)

5.if you want to see decompiled code on terminal(standard output),use command(see screenshot for example ): 

`uncompyle6 <filename.pyc>`

![Screenshot from 2017-07-01 13-39-59.png](https://gauravssnl.files.wordpress.com/2017/07/screenshot-from-2017-07-01-13-39-59.png)

Thanks for reading my post.I hope this will be useful for python users who want to decompile compiled python files.

 

 

 

 
