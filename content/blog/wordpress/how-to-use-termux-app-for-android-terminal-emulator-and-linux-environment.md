Title: How to use Termux App for Android : Terminal Emulator and Linux environment
Date: 2017-01-15 11:20
Author: gauravssnl
Category: Android
Slug: how-to-use-termux-app-for-android-terminal-emulator-and-linux-environment
Status: published

Termux is an **Android terminal emulator and Linux environment app **that works directly with no rooting or setup required. A minimal base system is installed automatically.Additionall packages are available using the APT package manager.

*Developer:* **Fredrik Fornwall**

Download link: [https://termux.com](http://termux.com) 

**Screenhsot**

![screenshot_20161231-080757](https://gauravssnl.files.wordpress.com/2017/01/screenshot_20161231-080757.png)

 

**Steps and Instructions** :

1.Download Termux app and install it.Open Termux and wait for its complete installation.

![screenshot_20161231-080835](https://gauravssnl.files.wordpress.com/2017/01/screenshot_20161231-080835.png)

2.Now, for first time you need to use this command (as shown in screenshot):
```bash
apt update 
```
![screenshot_20161231-081205](https://gauravssnl.files.wordpress.com/2017/01/screenshot_20161231-081205.png)

3.Now,we can use  `apt` command. To know how to use `apt` , click on Help in Termux app  (Long press in Termux Terminal window will bring menu ).

![https://gauravssnl.files.wordpress.com/2017/01/screenshot_20161231-082925.png?w=324&h=576](https://gauravssnl.files.wordpress.com/2017/01/screenshot_20161231-082925.png?w=324&h=576) ![https://gauravssnl.files.wordpress.com/2017/01/screenshot_20161231-083547.png?w=324&h=576](https://gauravssnl.files.wordpress.com/2017/01/screenshot_20161231-083547.png?w=324&h=576)

 

4\. To get list of available packages,use this command:

```bash
apt list
```

![screenshot_20161231-083450](https://gauravssnl.files.wordpress.com/2017/01/screenshot_20161231-083450.png)

5\. To install any package,say python ,use this command:
```bash
apt install python
```
![screenshot_20161231-081311](https://gauravssnl.files.wordpress.com/2017/01/screenshot_20161231-081311.png)

 

6\. To search any package,say python. Use this command:
```bash
apt search python
```

![screenshot_20161231-081311](https://gauravssnl.files.wordpress.com/2017/01/screenshot_20161231-081311.png)

7\. To remove/uninstall a package,say python , use this command:
```bash
apt remove python
```
8\. To see installed packages, use this command:

```bash
apt list --installed
```

![Screenshot_20161231-090507.png](https://gauravssnl.files.wordpress.com/2017/01/screenshot_20161231-090507.png)

I hope this post will be useful to Android users who want to use Terminal with Linux environment on Android  without need of rooting their phone.

Thanks to my family and friends.

 

 
