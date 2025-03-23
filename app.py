from flask import Flask, render_template
from datamanager.sqlite_data_manager import SQLiteDataManager

app = Flask(__name__)
data_manager = SQLiteDataManager('instance/moviwebapp.db')

@app.route('/')
def home():
     """Welcome to Movie App"""
     return render_template('index.html')

@app.route('/users')
def list_users():
    users = data_manager.get_all_users()
    return render_template('users.html')








if __name__ == '__main__':
    app.run(debug=True)