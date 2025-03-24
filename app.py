from flask import Flask, request, redirect, url_for, render_template, flash
from datamanager.sqlite_data_manager import SQLiteDataManager

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages
data_manager = SQLiteDataManager('instance/moviweb.db')

# Home Route
@app.route('/')
def home():
    """
    WELCOME to movieweb app
    """
    return render_template('index.html')

# Users List Route
@app.route('/users')
def users_list():
    """
    Display a list of all users.
    """
    users = data_manager.get_all_users()
    return render_template('users.html', users=users)

# User Movies Route
@app.route('/users/<int:user_id>')
def user_movies(user_id):
    """
    Display a specific user's list of favorite movies.
    """
    user = data_manager.get_user_by_id(user_id)
    if not user:
        flash("User not found!", "error")
        return redirect(url_for('users_list'))
    movies = data_manager.get_user_movies(user_id=user_id)
    return render_template('user_movies.html', user=user, movies=movies)

# Add User Route
@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    """
    Add a new user to the application.
    """
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            data_manager.add_user(name=name)
            flash("User added successfully!", "success")
            return redirect(url_for('users_list'))
        else:
            flash("Name cannot be empty!", "error")
    return render_template('add_user.html')

# Add Movie Route
@app.route('/users/<int:user_id>/add_movie', methods=['GET', 'POST'])
def add_movie(user_id):
    """
    Add a new movie to a user's list of favorite movies.
    """
    user = data_manager.get_user_by_id(user_id)
    if not user:
        flash("User not found!", "error")
        return redirect(url_for('users_list'))

    if request.method == 'POST':
        name = request.form.get('name')
        director = request.form.get('director')
        year = request.form.get('year')
        rating = request.form.get('rating')

        if name and director and year and rating:
            data_manager.add_movie(user_id=user_id, name=name, director=director, year=year, rating=rating)
            flash("Movie added successfully!", "success")
            return redirect(url_for('user_movies', user_id=user_id))
        else:
            flash("All fields are required!", "error")

    return render_template('add_movie.html', user=user)

# Update Movie Route
@app.route('/users/<int:user_id>/update_movie/<int:movie_id>', methods=['GET', 'POST'])
def update_movie(user_id, movie_id):
    """
    Update details of a specific movie in a user's list.
    """
    user = data_manager.get_user_by_id(user_id)
    if not user:
        flash("User not found!", "error")
        return redirect(url_for('users_list'))

    movie = data_manager.get_movie_by_id(movie_id)
    if not movie or movie.user_id != user_id:
        flash("Movie not found!", "error")
        return redirect(url_for('user_movies', user_id=user_id))

    if request.method == 'POST':
        name = request.form.get('name')
        director = request.form.get('director')
        year = request.form.get('year')
        rating = request.form.get('rating')

        if name and director and year and rating:
            data_manager.update_movie(movie_id=movie_id, name=name, director=director, year=year, rating=rating)
            flash("Movie updated successfully!", "success")
            return redirect(url_for('user_movies', user_id=user_id))
        else:
            flash("All fields are required!", "error")

    return render_template('update_movie.html', user=user, movie=movie)

# Delete Movie Route
@app.route('/users/<int:user_id>/delete_movie/<int:movie_id>')
def delete_movie(user_id, movie_id):
    """
    Delete a specific movie from a user's list.
    """
    user = data_manager.get_user_by_id(user_id)
    if not user:
        flash("User not found!", "error")
        return redirect(url_for('users_list'))

    movie = data_manager.get_movie_by_id(movie_id)
    if not movie or movie.user_id != user_id:
        flash("Movie not found!", "error")
        return redirect(url_for('user_movies', user_id=user_id))

    data_manager.delete_movie(movie_id=movie_id)
    flash("Movie deleted successfully!", "success")
    return redirect(url_for('user_movies', user_id=user_id))

if __name__ == '__main__':
    app.run(debug=True)