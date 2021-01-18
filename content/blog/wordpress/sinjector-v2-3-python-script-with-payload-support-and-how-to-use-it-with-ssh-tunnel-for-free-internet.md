Title: SInjector v2.3 Python Script with Payload support and how to use it with SSH Tunnel for Free Internet
Date: 2016-08-26 17:32
Author: gauravssnl
Category: Android, GPRS HACKS, Python
Slug: sinjector-v2-3-python-script-with-payload-support-and-how-to-use-it-with-ssh-tunnel-for-free-internet
Status: published

Hello everyone.Now,I would like to share **SInjector** Python Script which supports SSH and VPN  with Payload feature(like HTTP Injector,eProxy,KPN Tunnel). **SInjector** Python Script can be used for free internet tricks with SSH or VPN Tunneling.Free Internet with Online privacy.I would like to thank it's developer **RedFox** who developed this script.Many have been searching Python script which works similar to apps like  **HTTP Injector** ,**eProxy** ,**KPN Tunnel** and the search finally ends with **SInjector** .

I will share how to configure/set SInjector Python Script to use SSH & for free internet.

**Developer: *Red Fox***

**Tools Required: **

1\. ***SInjector_v2.3.zip*** [SInjector \_v2.3.zip](http://upfile.mobi/WggR3QPipEI)

2.***Terminal*** application : [Terminal.apk](http://upfile.mobi/aDy0JAy4SOc)

**Note:** Python should be already installed.   To know about that,see my other posts.

**Script Screenshot:**

[![](http://gauravssnl.files.wordpress.com/2016/08/screenshot_2016-08-22-18-46-23.png){.wp-image-774 .alignnone .size-full width="720" height="1280"}](http://gauravssnl.files.wordpress.com/2016/08/screenshot_2016-08-22-18-46-23.png)

**Steps:**

1.Download **SInjector v2.3.zip** file and extract to **si** folder of internal sdcard (**/sdcard/si)**.

2.Open **payload.ini** file and set Payload which works for free internet on your simcard as shown in screenshot and Save the file.Use your imagination to fill working payload.For my simcard , payload working for free internet is shown here in screenshot.(My simcard has free homepage which I can open at 0 balance and I use that in payload bug.You use your free homepage in payload and use your simcard Proxy in this file)

![](http://i0.wp.com/gauravssnl.files.wordpress.com/2016/08/screenshot_2016-08-07-13-16-01.png?w=528){.wp-image-775 .alignnone .size-full}

3.You should have a SSH account that we will use with **SSH Tunnel** application. To know how to do this, see my another post: [Using SSH Tunnel on Android Phones to Hide your real IP details and to Access Blocked Websites](https://gauravssnl.wordpress.com/2016/08/26/using-ssh-tunnel-on-android-phones-to-hide-your-real-ip-details-and-to-access-blocked-websites/)

I created SSH account on [fastssh.com](http://fastssh.com) as shown in screenshot.

![](http://i0.wp.com/gauravssnl.files.wordpress.com/2016/08/screenshot_2016-08-05-00-24-06.png?w=528){.wp-image-768 .alignnone .size-full}

4.Now,open SSH Tunnel application and fill your user details and SSH account Host correctly as shown in screenshot.You can tick/enable "SOCKS Proxy" if you want to use it for forwarding Request from all ports.If your phone is rooted you can also enable/tick "Global Proxy" to proxify all apps.

![](http://i0.wp.com/gauravssnl.files.wordpress.com/2016/08/screenshot_2016-08-07-14-12-21.png?w=528){.wp-image-769 .alignnone .size-full}

5.Do not change other remaining settings of SSH Tunnel application.Leave other settings as it is.Minimise or close this app.

6.Now,use your simcard  on which you want to use free internet.My simcard have 0(zero) balance which I will use for free internet.Now,I will connect internet using this sim .

7.Open Terminal application and change your directory to **si** folder where you have extracted those files in step 1.My **si** folder is located at **/sdcard/si** .So,i will type this on terminal to run the si.py file.Type these commands carefully and correctly:
```bash
cd /sdcard/si
su
```
8.Now run the **si.py** script using python command.If everything is correct,**SInjector** script will be running on your Terminal. It will ask for payload file location(default payload file is **payload.ini** which we will use),so type *n* and press enter key.See screenshot.

9.Now,script will ask you "Do you want to disable debug?", you can enter either *y* for YES or *n* for NO. It is your wish.See Screenshot

10.Now,script will ask "Auto Replace 200 OK", enter *y*** **and press Enter key.The Script will show local port  on which the script is accepting connections(in my Screenshot it is listening on port ** 9000** ).Notice this port carefully as we will use this port in next step.

11.Now,open SSH Tunnel application again and Tick/Enable "**Upstream Proxy** " and Put this  in "Proxy ": **127.0.0.1:9000** as SInjector script is listening on port 9000(shown in screenshot).you use your port on which **SInjector** script is listening.

[![](http://gauravssnl.files.wordpress.com/2016/08/screenshot_2016-08-07-14-12-31.png){.wp-image-776 .alignnone .size-full width="720" height="1280"}](http://gauravssnl.files.wordpress.com/2016/08/screenshot_2016-08-07-14-12-31.png)

12.Everything is finally done now.Now,Click on "**Tunnel Switch** " in SSH Tunnel app and minimize it(send it to background).

13.Now,open the **Terminal** app which is already running.If everything is correct and your payload is working for free internet,you will get `200 Connection Established` **Response** from SSH server as shown in my screenshot.

![](http://i0.wp.com/gauravssnl.files.wordpress.com/2016/08/screenshot_2016-08-22-18-46-23.png?w=528){.wp-image-774 .alignnone .size-full}

All steps are completed successfully.Now,you can open any application and use free internet.Your real IP address is hidden as you are using SSH.You can also try to use this **SInjector** Python script directly and VPN also in the same way.

Happy Free Internet phreaking .

Thanks for reading this long post.I hope my post will be useful for them who are new to Free Internet tricks and who do not know how to use the ** SInjector** Python script with **SSH** .

Thanks to everyone and my friends.If you have any questions or you get any error ,please post in **Comments.**

©gauravssnl
