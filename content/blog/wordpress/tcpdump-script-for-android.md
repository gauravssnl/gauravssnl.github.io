Title: TCPDUMP SCRIPT FOR ANDROID
Date: 2016-08-27 15:36
Author: gauravssnl
Category: Android
Slug: tcpdump-script-for-android
Status: published

Hello,everyone.Now,I want to share tcpdump script for Andriod and how to use it.Before doing that,let me tell what [tcpdump](https://en.wikipedia.org/wiki/Tcpdump) is.On Wikipedia,tcpdump is described as:

**tcpdump** is a common packet analyzer that runs under the command line. It allows the user to display TCP/IP and other packets being transmitted or received over a network to which the computer is attached. Distributed under the BSD license,tcpdump is free software.

tcpdump works on most Unix-like operating systems: Linux, Solaris, BSD, OS X, HP-UX, Android and AIX among others. In those systems, tcpdump uses the libpcap library to capture packets. The port of tcpdump for Windows is called WinDump; it usesWinPcap, the Windows port of libpcap.

**tcpdump **can be used for intercepting(capturing) the data packets sent by Android phone as it has Linux kernel.

**DOWNLOAD :**  [tcpdump](http://www.strazzere.com/android/tcpdump)

**STEPS:**

1.First trick:

Download and move *tcpdump *script to **/system/bin** folder using file manager like Xplore File manager. Use Xplore or any Filemanager with "Superuser + Mount" mode for changing file permissions.Now,go to  */system/bin/tcpdump* file and change its permission to **777** as shown in screenshot.

Note: Your **/system** folder must have read & write permission.

![Screenshot_2016-08-24-22-51-34](https://gauravssnl.files.wordpress.com/2016/08/screenshot_2016-08-24-22-51-34.png)

Another trick:

Consider that **tcpdump** script which i downloaded is in **/sdcard/download** folder.Then you can type these commands in terminal to copy file **tcpdump** to **/system/bin** and for changing file permission of **tcpdump** to *777* (see screnshot).Type these in terminal carefully as shown in screenshot:

![Screenshot_2016-08-24-23-18-22](https://gauravssnl.files.wordpress.com/2016/08/screenshot_2016-08-24-23-18-22.png)

```bash
su
mount -o remount,rw  /system
cp /sdcard/download/tcpdump /system/bin
cd /system/bin
chmod 777 tcpdump
mount -o remount,ro /system
```
2.Now,you have succesfully placed **tcpdump** in **/system/bin**.To run **tcpdump**, simply type this on Terminal as shown in screenshot:

`tcpdump`

![Screenshot_2016-08-24-23-39-10.png](https://gauravssnl.files.wordpress.com/2016/08/screenshot_2016-08-24-23-39-10.png)

You can clearly see **tcpdump** running and all data packets sent on Terminal screen.

If you want to save this log to a file *l.cap* for later analysis ,you can use this command in Terminal as shown in screenshot :
```bash
tcpdump -vv -s 0 -w /sdcard/l.cap
```

![Screenshot_2016-08-24-23-18-22](https://gauravssnl.files.wordpress.com/2016/08/screenshot_2016-08-24-23-18-221.png)

The options used are explained as:

**-vv :** puts tcpdump into verbose mode

**-s 0 :** sets the program to grab all packets

**-w :** writes the output to a file

The output file l.cap generated will be as shown in screenshot.This file can be analyzed application using Wireshark.

![Screenshot_2016-08-24-23-20-25](https://gauravssnl.files.wordpress.com/2016/08/screenshot_2016-08-24-23-20-25.png)


Now,you successfully know how to use tcmpdump to intercept all data packets.

Happy phreaking brothers.

Thanks everyone for reading this post.Thanks to my friends and facebook groups where i learn.

If you have any questions,please post in comments.

Sharing is caring.

©gauravssnl

 
