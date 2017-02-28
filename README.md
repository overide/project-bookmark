# Bookmark
It is a webapp which will let you save/bookmark images from different websites to your account and share them with your followers

## Apps
Following apps are installed in project - 
* **Images** : Manages image upload, edit, share, like etc.
* **Account** : Manages authentication etc.
* **Action** : Manage user actions

## Requirements
Before running project make sure you have installed all the dependencies.

1. First move to the directory which have *requirement.txt* file
2. Activate your virtual environment (optional)
3. Run following command 
```
>>> pip install -r requirements.txt
```
Make sure your **redis** server is up and running. To check status of redis server type following command in shell in **Ubuntu**
```
>>> service redis status
```
If server is not active type this command in shell to activate it
```
>>> sudo service redis start 
```
## Important settings 
Update **settings.py** file and change following values as per requirments to configure the project
Email Configuration
* **EMAIL_HOST** : Default is *'smtp.gmail.com'*
* **EMAIL_HOST_USER** : Default is  *'youremail@gmail.com'*
* **EMAIL_HOST_PASSWORD** : Default is *'password'*
* **EMAIL_PORT** : Default is *587*

Redis Configuration
* **REDIS_HOST** : Default is *'localhost'*
* **REDIS_PORT** : Default is  *6379*
* **REDIS_DB** : Default is *0*

## Running project
After installing all dependencies and configuration you can run the project at localhost by typing following commands - 
```
>>> python manage.py runserver
```
Access the project at **127.0.0.1:8000**

## Usages
1. Drag **Bookmark it** button to your browser bookmark toolbar
2. To bookmark images from other websites, click on that **Bookmark it** in your bookmark toolbar
3. Click on selected image to bookmark it

## Notes
* If you are running this project in localhost, for **https** websites, our application might not work.
* In settings.py DEBUG is True, if you are not running this project in development environment, set it to False

## Project Snapshots
* **Dashboard**
![alt text](https://github.com/overide/project-bookmark/blob/master/project_snapshots/bmark_dashboard.png "Dashboard")

* **Bookmarklet**
![alt text](https://github.com/overide/project-bookmark/blob/master/project_snapshots/bmark_bookmarklet.png "Bookmarklet")

* **Bookmarked Images**
![alt text](https://github.com/overide/project-bookmark/blob/master/project_snapshots/bmark_images.png "Bookmarked Images")

* **People Detail**
![alt text](https://github.com/overide/project-bookmark/blob/master/project_snapshots/bmark_people_detail.png "People Detail")

* **Image Detail**
![alt text](https://github.com/overide/project-bookmark/blob/master/project_snapshots/bmark_image_detail.png "Image Detail")

Image credits : http://poolga.com
