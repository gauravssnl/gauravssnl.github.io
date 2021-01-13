Title: How to get Facebook Note/Post comments by using Facebook API
Date: 2018-04-10 13:28
Author: gauravssnl
Category: API, Faceboook, Python
Slug: how-to-get-facebook-note-post-comments-by-using-facebook-api
Status: published

In this post, I am sharing how  we can get all the comments of a Facebook Post/Note by using Facebook API.

Recently, I tried to retrieve comments on my Facebook Notes by using Facebook Note API, but I found that Note API had been depreciated and could not be used.

![fb1](https://gauravssnl.files.wordpress.com/2018/04/fb1.png){.alignnone .size-full .wp-image-1952 width="1309" height="253"}

I thought that I won't be able to get comments on my Facebook Notes . But, I finally found a way to do so after playing with API for some days.

Many users may be trying to get all the comments on their Facebook Notes as Notes may contain many important links, tutorials,etc. This method can also be used for getting comments of Facebook Posts also.

Facebook Notes can be considered similar to that of Facebook  Posts. To get comments of any facebook Note/Post, we need its unique post-id whose prefix part is always profile-id\_ and last part is numerical part of Note URL.

You need to visit [<https://developers.facebook.com/tools/explorer/>]{style="color:#3366ff;"} and get your Graph API Access Token for using Facebook [[Graph API Explorer]{._51-3}]{._c24 ._50f4 ._50f7} .Just selelct all those permission which you want to use.

**Getting Facebook Profile Name & ID:**

![fb2](https://gauravssnl.files.wordpress.com/2018/04/fb2.png){.alignnone .size-full .wp-image-1953 width="1505" height="245"}

**Selecting any Facebook Note/Post and getting its last Numerical part of URL:**

![Screenshot from 2018-04-10 17-00-38.png](https://gauravssnl.files.wordpress.com/2018/04/screenshot-from-2018-04-10-17-00-38.png){.alignnone .size-full .wp-image-1954 width="1102" height="652"}

**Getting Facebook Note/Post post-id**

Now, we can easily form this Note post-id by adding profile-id and last numerical part of URL as shown in screenshot( profile-id +underscore + last numerical part of URL).

![fb4](https://gauravssnl.files.wordpress.com/2018/04/fb4.png){.alignnone .size-full .wp-image-1955 width="1477" height="233"}

By using the above method we can easily get Facebook Note ID .But, we have to do things manually each time for different posts/notes each time we want to retrieve comments. So, this method will inefficient.Thus, we should use different method as described below.

**Tools Required:**

1\. [[python 3]{style="color:#3366ff;"}](https://www.python.org/downloads/)

2.  [[facebook-sdk](http://facebook-sdk.readthedocs.io/en/latest/)]{style="color:#3366ff;"} (python module)

you can easily install facebook-sdk by using pip as shown below:

[pip install facebook-sdk]{style="color:#ff0000;"}

3. [ [FBNotes](https://github.com/gauravssnl/FBNotes/archive/master.zip) ]{style="color:#3366ff;"}

Download the above file and Extract it. Change your working directory to the directory where you extracted the files.

Edit **fb_notes.py** with your access token & other options as described below , then run the python script as shown below.

[python fb_notes.py]{style="color:#ff0000;"}

![Screenshot from 2018-04-10 16-26-57.png](https://gauravssnl.files.wordpress.com/2018/04/screenshot-from-2018-04-10-16-26-57.png){.alignnone .size-full .wp-image-1959 width="1920" height="1080"}

[[Using facebook-sdk]{style="color:#ff00ff;text-decoration:underline;"} ]{style="text-decoration:underline;"}

If you see the second screenshot, you can see that I had created my Facebook Note on 10 February  2017. I have used that date in my code to get posts created on that day .Using this approach, we can limit time-period to get posts and their post-id. Thus, this approach makes work easy.

You should use your own Facebook Note/Post date on which you created it.

**1. Getting Facebook Profile Name & ID :**

\[sourcecode language="python" wraplines="false" collapse="false"\]\
import facebook\
token = "YOUR_ACCESS_TOKEN"\
account_data = graph.get_object("me")\
print("Name:", account_data\["name"\])\
print("Profile ID: ", account_data\["id"\])\
\[/sourcecode\]

**2. Selecting Facebook Note/Post & Getting its post-id**

\[sourcecode language="python" wraplines="false" collapse="false"\]\
posts = graph.get_object("me/feed?since=10 February 2017 & until=11 February 2017")\
note_data = posts\["data"\]\[0\]\
print("Post/Note Title: ",note_data\["message"\])\
note_postid = note_data\["id"\]\
print("Post/ Note ID: ", note_postid)\
\[/sourcecode\]

**3. Getting Comments & total number of comments**\
\[sourcecode language="python" wraplines="false" collapse="false"\]\
\# get comment data . Not all comments will be returned by facebook API\
comments_data = graph.get_object(note_postid + "/comments")\
\# get total number of comments\
comments_data = graph.get_object(note_postid + "?fields=comments.summary(true)")\
comments_count = comments_data\["comments"\]\["summary"\]\["total_count"\]\
print("Post/Note Comments count: ", comments_count)\
\[/sourcecode\]

**4. Getting total comments on Facebook Note/Post**\
\[sourcecode language="python" wraplines="false" collapse="false"\]\
comments_data = graph.get_object(note_postid + "/comments?limit=" + str(comments_count))\
cc = 0\
print("No.","\\t", "Comment")\
for comment in comments_data\["data"\]:\
print(cc," ", comment\["message"\])\
cc += 1\
\[/sourcecode\]

**Complete Code**

![Screenshot from 2018-04-10 18-32-17](https://gauravssnl.files.wordpress.com/2018/04/screenshot-from-2018-04-10-18-32-17.png){.alignnone .size-full .wp-image-1962 width="1920" height="1080"}

Now,edit your access token & other things as described above  depending upon your requirements, then run the python script as shown below.

[python  fb_notes.py]{style="color:#ff0000;"}

**Output :**

![Screenshot from 2018-04-10 16-29-14.png](https://gauravssnl.files.wordpress.com/2018/04/screenshot-from-2018-04-10-16-29-14.png){.alignnone .size-full .wp-image-1960 width="1920" height="1080"}

We can also save the comments in a file for later use.By using the above methods , we can get Facebook Notes/Posts comments and other data.

I hope this post will be useful for them who want to use Facebook API & its python SDK.

If you have any questions or you face any problem, please post them in comments.

Thanks for reading the post. Share it with others, if you like it.
