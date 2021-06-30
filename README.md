# E-Commerce-Application-APIs-using-Django

### Objective:
In this project the backend part of the E-Commerce Application is developed using Django Rest Framework

### Structure:
There will be 3 tables in the database
1. Customer Order Table –  Stores ordered items from the customer side
2. Inventory management Table – helps to visualize the current State of a Certain Warehouse
3. Purchase Order Table – Place the orders to be purchased from the specified Supplier


### Workflow:
The following picture shows, how Django Appllication actually interact with user end to Database and vice-versa.
![image](https://user-images.githubusercontent.com/86600232/124011917-288a3980-d9fe-11eb-93ae-f1c93240da00.png)

## Installation and Setup: 
Open command prompt and choose desired folder

### Create a Virual Environment
```
python -m venv <enviornment name>
```

### Activate the Virtual Environment
```
<enviornment name>\Scripts\activate
```

### Install Django
```
pip install django
```

### Install Django Rest Framework
```
pip install djangorestframework
```

### Create Django Project
```
django-admin startproject <project name>
```

Go inside the Django Project folder

### Open Visual Studio Code
```
code .
```

Open another command prompt and go inside the project folder,activate the virtual environment

### Run the server
```
python manage.py runserver
```

Open your browser and go to http://127.0.0.1:8000/ , you will see the following image

![djangoRunServer](https://user-images.githubusercontent.com/86600232/124022576-9b99ad00-da0a-11eb-951d-641aab7fe79b.png)
