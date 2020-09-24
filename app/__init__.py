from flask import Flask, render_template, request, url_for
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '...'))
static = os.path.abspath("static")
SECRET_KEY = os.environ.get('SECRET_KEY') or 'burasidegisecek'

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(
    os.path.join(project_dir, "shopbasket.db"))

app = Flask(__name__, static_folder=static)
app.static_folder = 'static'
app.config['SECRET_KEY'] = SECRET_KEY

