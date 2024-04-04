# from flask import flash
from sqlalchemy import create_engine, text
import os

db_connection_str = os.environ['DB_CONN_STRING']


# Create the engine
engine = create_engine(db_connection_str, connect_args={
    "ssl": {
        "ca": "ca.pem",  # replace with the path to your CA certificate
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

# Load movies from the database
def load_movies_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from movies"))
    movies = []
    for movie in result.all():
        movies.append(movie._asdict())
    # print(movies)
    # print(type(movies))
    return movies

# Load movie from the database
def load_movie_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM movies WHERE id = :val"), {'val': id})
    rows = result.all()
    if len(rows) == 0:
      # print("Movie Not Found")
      return None
    else:
      # print(rows[0]._asdict())
      return rows[0]._asdict()

# Load rating from the database
def load_rating_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT movie_id, ROUND(AVG(rating), 2) AS avg_rating FROM ratings WHERE movie_id = :val GROUP BY movie_id"), {'val': id})
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      # print(rows[0]._asdict())
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
def check_movie(name, genre):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM movies WHERE movie_name = :m_name AND genre = :g_name"), {'m_name': name, 'g_name': genre})
    rows = result.all()
    if len(rows) == 0:
      return False
    else:
      return True