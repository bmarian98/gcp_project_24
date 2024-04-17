from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def root_path():
    environment = os.getenv('FLASK_ENV', 'prod')

    hostname = os.getenv('HOSTNAME', 'xyz')

    return render_template('index.html', environment=environment, hostname=hostname)