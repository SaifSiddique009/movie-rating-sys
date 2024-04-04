# from flask import flash
from sqlalchemy import create_engine, text
import os

db_connection_str = os.environ['DB_CONN_STRING']


# Create the engine
engine = create_engine(db_connection_str, connect_args={
    "ssl": {
        "ca": "ca.pem",  
    },
})

# try:
#     with engine.connect() as conn:
#         # conn.execute(text("CREATE TABLE mytest (id INTEGER PRIMARY KEY)"))
#         conn.execute(text("INSERT INTO mytest (id) VALUES (1), (2)"))
#         result = conn.execute(text("SELECT * FROM mytest"))
#         print(result.fetchall())
# except Exception as e:
#     print(f"Error: {e}")

# Load user from the database
def load_user_from_db(email, password):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM users WHERE email = :email AND password = :password"), {'email': email, 'password': password})
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()

# Load movies from the database
def load_movies_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from movies"))
    movies = []
    for movie in result.all():
        movies.append(movie._asdict())
    return movies

# Load movie from the database
def load_movie_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM movies WHERE id = :val"), {'val': id})
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()

# Load rating from the database
def load_rating_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT movie_id, ROUND(AVG(rating), 2) AS avg_rating FROM ratings WHERE movie_id = :val GROUP BY movie_id"), {'val': id})
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()

# Merge movie and rating data into movie
def load_full_movie_details(id):
  movie = load_movie_from_db(id)
  rating = load_rating_from_db(id)

  avg_key = 'avg_rating'

  if not movie:
    # flash('Logged in successfully!', category='success')
    return "Not Found", 404
  elif rating is not None and avg_key in rating:
    movie[avg_key] = rating[avg_key]
  else:
    movie[avg_key] = "Not avialable"
  return movie

# Check movie's existance in the database
def check_movie(name, genre, rating, release_date):
  print("Release Date ", release_date)
  print("Type", type(release_date))
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM movies WHERE name = :m_name AND genre = :g_name AND rating = :r_name AND release_date = :r_date"), {'m_name': name, 'g_name': genre, 'r_name': rating, 'r_date': release_date})
    rows = result.all()
    print("Existance of Movie", rows)
    if len(rows) == 0:
      result = conn.execute(text("INSERT INTO movies (name, genre, rating, release_date) VALUES (:name, :genre, :rating, :release_date)"), {'name': name, 'genre': genre, 'rating': rating, 'release_date': release_date})
      conn.commit()
    else:
      return True

# Search movie in the database
def search_movie(name):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM movies WHERE name = :m_name"), {'m_name': name})
    rows = result.all()
    if len(rows) == 0:
      return False
    else:
      return rows[0]._asdict()

# Update movie to the database
def update_info(movie, rating):
  with engine.connect() as conn:
    conn.execute(text("INSERT INTO ratings (user_id, movie_id, rating) VALUES (:user_id, :movie_id, :rating)"), {'user_id': 4, 'movie_id': movie['id'], 'rating': rating})
    conn.commit()
    print("Movie Id", movie['id'])
    
  result = load_full_movie_details(movie['id'])
  print("Updated Movie", result)
  return result