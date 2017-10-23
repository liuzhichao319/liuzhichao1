
from server import app
from flask import render_template

@app.route('/')
def hello_world():
    return "Hello from Python!"

@app.errorhandler(404)
@app.route("/error")
def page_not_found(error):
    return "Sorry, this page does not exist", 404
