# Bookmark
It is a webapp which will let you save/bookmark images from different website to your account and share with your followers

## Apps
Following apps are installed in project - 
* **Images** : Manages image upload, edit, share, like etc.
* **Account** : Manages authentication etc.
* **Action** : Manage user actions

## Requirments
Before running project make sure you have installed all the dependencies.

1. First move to the directory which have *requirment.txt* file
2. Activate your virtual environment (optional)
3. Run following command 
```
>>> pip install -r requirments.txt
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

## Running projectfjbfbf
After installing all dependencies and configuration you can run the project at localhost by typing following comma - 
```
Access the project at **127.0.0.1:8000**
>>> python manage.py runserver
```
