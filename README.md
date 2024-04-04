# Movie Rating System

This project is a movie rating system website with a focus on the backend side. The website is built using Flask and SQLAlchemy, and it uses a cloud database from Aiven.io (MySQL). The website is deployed using a free resource called Render.

## Features

The website has the following features:

1. User login
2. Adding a movie
3. Viewing a list of all movies
4. Rating a movie
5. Searching for a specific movie and viewing its details along with the average rating

## Code Structure

The project consists of two main Python files: `app.py` and `database.py`.

### app.py

This file contains the Flask application and the routes for the different pages of the website. Here is a brief overview of the routes:

- `'/'`: The login page. Users can log in with their email and password.
- `'/home'`: The home page. It displays a list of all movies.
- `'/home'` (POST): The search movie page. Users can search for a specific movie.
- `'/api/home/movies'`: An API endpoint that returns a list of all movies in JSON format.
- `'/movie/<id>'`: The movie page. It displays the details of a specific movie.
- `'/api/movie/<id>'`: An API endpoint that returns the details of a specific movie in JSON format.
- `'/add'`: The add movie page. Users can add a new movie.
- `'/rate/<id>'`: The rate movie page. Users can rate a specific movie.

### database.py

This file contains functions for interacting with the database. Here is a brief overview of the functions:

- `load_user_from_db(email, password)`: Loads a user from the database.
- `load_movies_from_db()`: Loads all movies from the database.
- `load_movie_from_db(id)`: Loads a specific movie from the database.
- `load_rating_from_db(id)`: Loads the rating of a specific movie from the database.
- `load_full_movie_details(id)`: Merges the movie and rating data into a movie.
- `check_movie(name, genre, rating, release_date)`: Checks if a movie exists in the database.
- `search_movie(name)`: Searches for a movie in the database.
- `update_info(movie, rating)`: Updates a movie in the database.

## How to Run

To run this project on your local machine, follow these steps:

1. Clone the repository.
2. Install the required packages (Flask and SQLAlchemy).
3. Set up the environment variable `DB_CONN_STRING` with your database connection string.
4. Run `app.py`.

Please note that you need to have a MySQL database set up on Aiven.io, and you need to populate the database with sample users, movies, and ratings.

You can visit the live site [here](https://movie-rating-sys.onrender.com). Please note that as this is a free resource, you might need to wait for 1 to 2 minutes for the site to fully load. You can log in with a sample user from the given dataset to view the site. For example, the user email address is `john_doe@gmail.com` and the password is `pass1`. After logging in, you will be directed to the home page, where you will see a list of movies from the database. You can add new movies, search for a movie from the database, and rate a movie. The average rating of each movie is calculated and displayed on the movie info page.