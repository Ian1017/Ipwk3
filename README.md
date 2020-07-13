# Album 
## Author  

>[Ian Mdawida](https://github.com/ian1017/ipwk3)  
  
# Description  
This is a Django application for displaying different projects and different users can vote on them based on their usability,design and content.

##  Live Link  
Click https://django-heroku-album.herokuapp.com/ to visit the webite
## Screenshots 
###### Home page

## User Story  

* View posted projects and their details
* Post a project to be rated/reviewed
* Rate/ review other users' projects
* Search for projects   
* View projects overall score
* View my profile page

## Setup and Installation  
To get the project .......  

##### Cloning the repository:  
 ```bash 
https://github.com/ian1017/ipwk3
```
##### Navigate into the folder and install requirements  
 ```bash 
cd ipwk3 pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations awwards 
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py server 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  


## Technology used  

* [Python3.8](https://www.python.org/)  
* [Django 2.0](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  

## Contact Information   
If you have any question or contributions, please email me at [mdawidamengo@gmail.com]  
## License 

* Copyright (c) 2020 **Ian Mdawida**