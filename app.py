from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from database import load_full_movie_details, load_movies_from_db, check_movie, search_movie, update_info, load_user_from_db

app = Flask(__name__)
app.secret_key = 'sdfasdf fsdfjasdf'

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
    user = load_user_from_db(email, password)
    if user:
      return redirect(url_for('home'))
    else:
      return render_template('login.html', error='Invalid email or password')
  return render_template('login.html')

# Home Page
@app.route('/home')
def home():
  movies = load_movies_from_db()
  return render_template('home.html', movies= movies)

# Search Movie Page (Need to work more)
@app.route('/home', methods = ['POST'])
def search_movie_page():
  movie_name = request.form.get('search')
  # print(movie_name)
  movie_status = search_movie(movie_name)
  print(movie_status)
  if not movie_status:
    return 'Not Found'
  return render_template('moviepage.html', movie=movie_status)
  

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
    rating = request.form.get('rating')
    release_date = request.form.get('release_date')
    # print(movie_name, genre)
    movie_status = check_movie(movie_name, genre, rating, release_date)
    if movie_status:
      return jsonify('Movie already exists')
    else:
      return redirect(url_for('home'))
  
  return render_template('add_movie.html')

# Rate Movie
@app.route("/rate/<id>", methods = ['GET', 'POST'])
def rate_movie(id):
  movie = load_full_movie_details(id)
  
  if request.method == 'POST':
    rating = request.form.get('add_rating')
    if rating is not None and len(rating) != 0:
        try:
            rating_float = float(rating)
            print("App.py", movie)
            update_movie = update_info(movie, rating_float)
            print("App.py-Updated:", update_movie)
            return redirect(url_for('show_movie', id=movie['id']))
        except ValueError:
            print("The rating cannot be converted to a float.")
    else:
        print("No rating was provided.")
      
  return render_template('rate_movie.html', movie=movie)


# Call Main Function
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)