Title: How to decompile compiled .pyc python files to find/see original source code
Date: 2017-07-01 09:03
Author: gauravssnl
Category: Decompiling, Python, Reverse Engineering, Ubuntu, Windows
Slug: how-to-decompile-compiled-pyc-python-files-to-findsee-original-source-code
Status: published

Hello,everyone.In this post,i am sharing how to decompile compiled python files which are in .pyc formats usually.It may be useful for reverse enginering and if you want to know the original source code of any compiled python files.It may be also useful whenever  your original .py  python file is deleted unknowingly and there is only compiled .pyc file left  on disk and you want your original .py file back.In all those cases, this method can be used.

I have used Ubuntu OS here and it can be used on Windows OS also.

[**Tools Required :**]{style="color:#000000;"}

[**uncompyle6**]{style="color:#800000;"}[  ]{style="color:#ff0000;"}: <https://github.com/rocky/python-uncompyle6/>

[Thanks :]{style="color:#993366;"}[R. Bernstein (Author of uncompyle6)\
]{.p-name .vcard-fullname .d-block}

**[Steps : ]{style="color:#000000;"}**

1.Install [uncompyle6 ]{style="color:#ff0000;"}by using [pip ]{style="color:#ff0000;"} on Terminal or you can download from above link and install it by running its [setup.py ]{style="color:#ff0000;"}file.To install [uncompyle6 ]{style="color:#ff0000;"}by using [pip]{style="color:#ff0000;"},use this command on Terminal :

[pip install uncompyle6]{style="color:#ff0000;"}

 

2.After installation of  [uncompyle6 ]{style="color:#ff0000;"},you can check its successfull installation and its usage by running [uncompyle6 ]{style="color:#ff0000;"}command on Terminal (see screenshot).

 

3.To decompile any file in current diectory ,use command (see screenshot for example): [uncom]{style="color:#ff0000;"}[pyle6 -o . \<file-name.pc\>  ]{style="color:#ff0000;"}

Example : [uncompyl6 -o . txfile.pyc rxfile.pyc]{style="color:#000000;"}

![Screenshot from 2017-07-01 13-38-05](https://gauravssnl.files.wordpress.com/2017/07/screenshot-from-2017-07-01-13-38-05.png){.alignnone .size-full .wp-image-1668 width="1920" height="1080"}

 

4.You will see your decompiled files created with same name in the current working directory(or desired directory) .Now,you can open this decompiled file with any Text Editor and see original source code.

![Screenshot from 2017-07-01 13-38-46.png](https://gauravssnl.files.wordpress.com/2017/07/screenshot-from-2017-07-01-13-38-46.png){.alignnone .size-full .wp-image-1677 width="1920" height="1080"}

 

5.if you want to see decompiled code on terminal(standard output),use command(see screenshot for example ): [uncompyle6 \<filename.pyc\> ]{style="color:#ff0000;"}

![Screenshot from 2017-07-01 13-39-59.png](https://gauravssnl.files.wordpress.com/2017/07/screenshot-from-2017-07-01-13-39-59.png){.alignnone .size-full .wp-image-1686 width="1920" height="1080"}

 

Thanks for reading my post.I hope this will be useful for python users who want to decompile compiled python files.

 

 

 

 
