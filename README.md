Personal-Gallery

## Author 
Ndundiro Kamau

## Description

Personal-gallery is a platform that allows a users to display their photos for world to see.Photos can be displayed according to  different categories and locations.



## SetUp/Installations
1. Download the zip file of the project or Clone the repository using the following command:
git clone ```https://github.com/Ndundiro/Personal-Gallery.git```

Navigate to the project directory
cd IP

2. Virtual Environment
Install virtualenv  using pip:
```python3.6 -m venv virtual```
Proceed to activate the virtual environment 
```source virtual/bin/activate```

3. Install packages/dependancies
Install the packages in the requirements.txt file:
```pip install -r requirements.txt```

4. Create a database
Create a new postgress database,Type the following command
psql
Run the following command,it creates a new database named gallery1
```#create database gallery1```

5. Create Database migrations
run the following command:
```python3 manage.py makemigrations gallery```
followed by:
```python3 manage.py migrate```

6. Run the app
To run the application:
```python3 manage.py runserver``` 

Open link given in a browser http://127.0.0.1:8000/.

to run tests:
```python3 manage.py test```

For more Information,Read the following documents:

* DjangoDocumentation
* PythonDocumentation

User Stories
1. As a user, I would like to view different photos that interest me.
2. As a user, I would like to click on a single photo to expand it and also view the details of the photo.The photo details must appear on a modalwithin the same route as the main page.
3. As a user, I would like to search for different categories of photos.eg Food,
4. As a user, I would like to copy a link to the photo to share with my friends.
5. As a user, I would like to view photos based on the location they were taken.



## Bugs
There are no known bugs yet

## Technologies Used
* Python3.6
* Django 1.11
* PostgreSQL
* HTML5
* CSS3
* Heroku

### Dependencies
* Postgresql

## Support and Contact Details
For any comments,suggestions,feedback or inquiries, contact me via email: ndundirokamau@gmail.com

## License
[MIT License](#)

Copyright © 2019 Ndundiro Kamau
