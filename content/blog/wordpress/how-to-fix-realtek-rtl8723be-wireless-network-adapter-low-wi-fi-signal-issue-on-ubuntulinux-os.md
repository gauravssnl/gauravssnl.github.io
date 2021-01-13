Title: How to fix Realtek RTL8723BE Wireless Network  Adapter Low Wi-Fi Signal Issue on Ubuntu/Linux OS
Date: 2017-06-18 09:48
Author: gauravssnl
Category: Linux, Networking, Ubuntu
Slug: how-to-fix-realtek-rtl8723be-wireless-network-adapter-low-wi-fi-signal-issue-on-ubuntulinux-os
Status: published

Hello,everyone.Today , I  want to share how to fix Realtek RTL8723BE Wireless Network Adapter Low Wi-Fi Signal Issue on Ubuntu/Linux OS.This tutorial can be also used for other Realtek Wireless Network Adapters supported by **rtlwifi_new **.

I have a great interest in using Using Ubuntu OS , so I installed latest version of Ubuntu OS alongside Windows OS.But, I faced low Wi-Fi signal issue on Ubuntu OS .Ubuntu OS failed to find many Wi-Fi networks which I could easily find & use on Windows OS.  Then,I started finding solutions to my problem and I found  a working solution.

[**Tools Required :**]{style="color:#000000;"}

# [rtlwifi_new]{style="color:#0000ff;"} : <https://github.com/lwfinger/rtlwifi_new>

[**Steps :**]{style="color:#000000;"}

1.Download **rtlwifi_new **from above link and extract it to Desktop (or to your desitrd folder).

2.Open **Terminal** and change your directory to the folder where you extracted rtlwifi_new zip file (here ,[ Desktop/rtlwifi_new-master]{style="color:#ff0000;"} )  by using [cd ]{style="color:#000000;"} command .See Screenshot given below :

[cd   Desktop/rtlwifi_new-master ]{style="color:#ff0000;"}

3.Now,run this command in Terminal as shown in Screenshot given below:

[make clean  ]{style="color:#ff0000;"}(optional for first time installation,you can use it for further installation)

[make ]{style="color:#ff0000;"}

[![Screenshot from 2017-06-18 12-17-22.png](https://gauravssnl.files.wordpress.com/2017/06/screenshot-from-2017-06-18-12-17-22.png){.alignnone .size-full .wp-image-1517 width="1920" height="1080"}]{style="color:#cc99ff;"}

 

4.After that ,run this command in terminal  as shown in screenshot given below:

[sudo make install  ]{style="color:#ff0000;"}

![Screenshot from 2017-06-18 12-19-13.png](https://gauravssnl.files.wordpress.com/2017/06/screenshot-from-2017-06-18-12-19-13.png){.alignnone .size-full .wp-image-1525 width="1920" height="1080"}

 

5.If everything is allright,you will see the message  **" Install rtlwifi SUCCESS  "** ** **. It means that **rtlwifi **has beeen installed successfully.

6.Now,run this command as shown in screenshot given below :

[sudo modprobe rtl8723be ]{style="color:#ff0000;"}

7.After that , run this command as shown in screenshot given below :

[echo "options rtl8723be ant_sel=2" \| sudo tee /etc/modprobe.d/rtl8723be.conf]{style="color:#ff0000;"}

8.This step is optional.If you want to see that  text contents are written successfully to **/etc/modprobe.d/rtl8723be.conf **.you can use this command  as shown in screenshot given below :

[cat /etc/modprobe.d/rtl8723be.conf]{style="color:#ff0000;"}

![Screenshot from 2017-06-18 12-27-53.png](https://gauravssnl.files.wordpress.com/2017/06/screenshot-from-2017-06-18-12-27-53.png){.alignnone .size-full .wp-image-1558 width="1920" height="1080"}

 

9.If all the above commands ae executed successfully,then everything has been done. Now,you need to **restart your computer** and you will see Wi-Fi working properly and your computer will find available Wi-Fi   networks in your area.

10.After restarting  your computer, select Wi-Fi network which you want to connect .

![Screenshot from 2017-06-18 12-35-14.png](https://gauravssnl.files.wordpress.com/2017/06/screenshot-from-2017-06-18-12-35-14.png){.alignnone .size-full .wp-image-1567 width="1920" height="1080"}

 

I hope this post will be useful for many users who use Realtek Wireless Network Adapter  and face low Wi-Fi signal issues on Ubuntu OS.

If you have any query or you face any problem ,please comment.Thank you for reading my post.

**Thanks** : **[lwfinger ]{style="color:#ff0000;"}( Author of rtlwifi_new)**

**Sources:**

1\. [ https://askubuntu.com/questions/645220/unable-to-connect-wifi-ubuntu-14-04-lts-hp-pavilion-network-driver-rtl8723be/729660\#729660  ](https://askubuntu.com/questions/645220/unable-to-connect-wifi-ubuntu-14-04-lts-hp-pavilion-network-driver-rtl8723be/729660#729660)

2. <https://askubuntu.com/questions/635625/how-do-i-get-a-realtek-rtl8723be-wireless-card-to-work/635629#635629>

3\. <https://connectwww.com/how-to-solve-realtek-rtl8723be-weak-wifi-signal-problem-in-ubuntu/4625/>

 

 

 
