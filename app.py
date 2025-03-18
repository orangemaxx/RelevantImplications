from flask import Flask, render_template, url_for, redirect
import os
import json
import shutil

with open("pages.json", "r") as file:
    pages = json.load(file)


app = Flask(__name__)

@app.route("/")
def index():
    return "Your static site has been generated in build/"

def savefile(filename, args):
    current_dir = os.path.dirname(__file__)
    rel_path = "/build/" + filename
    with open(current_dir + rel_path, "w") as f:
        f.write(render_template(filename, **args))

with app.app_context():
    for page in pages:
        args = pages[page]
        savefile(page, args)
    shutil.copytree("bootstrap/dist/js", "static/js", dirs_exist_ok=True)
    shutil.copytree("static/", "build/static", dirs_exist_ok=True)

app.run(debug=True)