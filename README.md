# Movie Rating System

This project is a movie rating system website with a focus on the backend. The website is built using Flask and SQLAlchemy, and it uses a cloud database from Aiven.io (MySQL). The website is deployed using a free resource called Render.

## Features

The website has the following features:

1. User login
2. Add a movie
3. View a list of all movies
4. Rate a movie
5. Search a specific movie and see its details along with the average rating

## Code Overview

The project consists of two main Python files: `app.py` and `database.py`.

### app.py

This file is the main entry point of the Flask application. It defines the routes for the website and the corresponding functions that should be executed when a user visits these routes. The routes include the login page, home page, movie page, add movie page, and rate movie page.

### database.py

This file contains functions for interacting with the database. It includes functions for loading a user from the database, loading movies from the database, checking if a movie exists in the database, searching for a movie in the database, and updating movie information in the database.

## How to Run the Project Locally

To run this project on your local machine, follow these steps:

1. Clone the project to your local machine.
2. Install the required Python packages by running `pip install -r requirements.txt`.
3. Set the `DB_CONN_STRING` environment variable to your Aiven.io MySQL database connection string.
4. Run the Flask application by executing `python app.py`.

Please note that when adding a movie, you must provide a proper date format (yyyy-mm-dd) for the movie release date, otherwise it will break the code. This issue will be fixed in a future update.

## Live Demo

You can visit the live demo of the site at [https://movie-rating-sys.onrender.com](https://movie-rating-sys.onrender.com). Please note that as this is a free resource, you might have to wait for 1 to 2 minutes for the site to fully load. To log in, you can use the sample user credentials: email - john_doe@gmail.com, password - pass1. After logging in, you will be directed to the home page where you can view a list of movies from the database, add new movies, search for a movie, and rate a movie. The average rating of each movie is calculated and displayed on the movie info page. 

## Future Work

In the future, more features will be added to the website, such as user registration, movie reviews, and more. Stay tuned for updates!