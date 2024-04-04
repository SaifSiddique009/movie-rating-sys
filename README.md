# Movie Rating System

This project is a movie rating system website with a focus on the backend side. The website is built using Flask and SQLAlchemy, and it uses a cloud database from Aiven.io (MySQL). The site is deployed using a free resource called Render.

## Features

The website includes the following features:

1. User login
2. Adding a movie
3. Viewing a list of all movies
4. Rating a movie
5. Searching for a specific movie and viewing its details along with the average rating

You can visit the site [here](https://movie-rating-sys.onrender.com). Please note that as this is a free resource, you might need to wait for 1 to 2 minutes for the site to fully load.

## Code Structure

The project consists of two main Python files: `app.py` and `database.py`.

### app.py

This file contains the Flask application and the routes for the different pages of the website. Here is a brief overview of the routes:

- `'/'`: The login page. Users can enter their email and password to log in.
- `'/home'`: The home page. It displays a list of all movies.
- `'/home'` (POST method): The search movie page. Users can search for a specific movie.
- `'/api/home/movies'`: An API that returns a list of all movies in JSON format.
- `'/movie/<id>'`: The movie page. It displays the details of a specific movie.
- `'/api/movie/<id>'`: An API that returns the details of a specific movie in JSON format.
- `'/add'`: The add movie page. Users can add a new movie.
- `'/rate/<id>'`: The rate movie page. Users can rate a specific movie.

### database.py

This file contains functions for interacting with the database. Here is a brief overview of the functions:

- `load_user_from_db(email, password)`: Loads a user from the database.
- `load_movies_from_db()`: Loads all movies from the database.
- `load_movie_from_db(id)`: Loads a specific movie from the database.
- `load_rating_from_db(id)`: Loads the rating of a specific movie from the database.
- `load_full_movie_details(id)`: Merges the movie and rating data into a movie.
- `check_movie(name, genre, rating, release_date)`: Checks the existence of a movie in the database.
- `search_movie(name)`: Searches for a movie in the database.
- `update_info(movie, rating)`: Updates a movie in the database.

## How to Run the Code Locally

To run the code locally, follow these steps:

1. Clone the repository to your local machine.
2. Install the required packages by running `pip install -r requirements.txt`.
3. Set the `DB_CONN_STRING` environment variable to your Aiven.io MySQL database connection string.
4. Run `python app.py`.

Please note that you need to have Python and pip installed on your machine. Also, you need to have an account on Aiven.io and create a MySQL database. Finally, you need to replace `'sdfasdf fsdfjasdf'` in `app.py` with your own secret key.