from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome in Flask application!"

@app.route('/about')
def about():
    return "This is the about page of Flask app"

if __name__ == '__main__':
    app.run(debug=True)
