import os
from flask import Flask, render_template, send_from_directory

# Correct paths from inside /api/
app = Flask(__name__, static_folder="../static", template_folder="../templates")

@app.route("/")
def index():
    return render_template("index.html")

app = app