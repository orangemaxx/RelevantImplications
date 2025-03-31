from flask import Flask, render_template, url_for, redirect
import os
import json
import shutil
from flask_compress import Compress

with open("pages.json", "r") as file:
    pages = json.load(file)



app = Flask(__name__)
compress = Compress()
compress.init_app(app)

buildDir = os.path.dirname(__file__) + "/build/"
if not os.path.exists(buildDir):
    os.makedirs(buildDir)

@app.errorhandler(404)
def index(e):
    return "Your static site has been generated in build/"

def savefile(filename, args, template):
    current_dir = os.path.dirname(__file__)
    rel_path = "/build/" + filename
    if not os.path.exists(os.path.dirname(current_dir + rel_path)):
        os.makedirs(os.path.dirname(current_dir + rel_path))
    with open(current_dir + rel_path, "w") as f:
        f.write(render_template("pages/"+template, **args))
        print("Created page: " + filename)

with app.app_context():
    # shutil.copytree("bootstrap/dist/js", "static/js", dirs_exist_ok=True)
    shutil.copytree("static/", "build/static", dirs_exist_ok=True)
    for page in pages:
        args = pages[page]["args"]
        template = pages[page]["template"]
        savefile(page, args, template)
    

# app.run(debug=True) # Only for working on it Comment this out