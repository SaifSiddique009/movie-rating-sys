from flask import Flask, render_template, request, jsonify
from database import load_full_movie_details, load_movies_from_db, check_movie

app = Flask(__name__)

# @app.before_request
# def before_request():
#     g.db = get_db_connection()

# @app.teardown_request
# def teardown_request(exception=None):
#     db = getattr(g, 'db', None)
#     if db is not None:
#         db.close()

# Login Page
@app.route('/', methods = ['GET', 'POST'])
def login():
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')
    print(email, password)
  return render_template('login.html')

# Home Page
@app.route('/home')
def home():
  movies = load_movies_from_db()
  return render_template('home.html', movies= movies)

# Home Page API
@app.route('/api/home/movies')
def list_jobs():
  movies = load_movies_from_db()
  return jsonify(movies)

# Movie Page
@app.route("/movie/<id>")
def show_movie(id):
  movie = load_full_movie_details(id)
  if movie == 'Not Found':
    return 'Not Found'

  return render_template('moviepage.html', 
                         movie=movie)
# Movie Page API
@app.route("/api/movie/<id>")
def show_movie_json(id):
  movie = load_full_movie_details(id)
  return jsonify(movie)

# Add Movie
@app.route("/add", methods = ['GET', 'POST'])
def add_movie():
  if request.method == 'POST':
    # Assuming there won't be any movie with same name and genre
    movie_name = request.form.get('movie_name')
    genre = request.form.get('genre')
    # print(email, password)
    movie_status = check_movie(movie_name, genre)

    if not movie_status:
      # movie database e nai, tai new movie entry korbo
      
  
  return render_template('add_movie.html')

# Search Movie

# Rate Movid

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)