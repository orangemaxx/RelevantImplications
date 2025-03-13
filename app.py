from flask import Flask, render_template, url_for
import os
import json

with open("pages.json", "r") as file:
    pages = json.load(file)


app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("index.html", name="Relevent Implications")


def savefile(filename, args):
    current_dir = os.path.dirname(__file__)
    rel_path = "/build/" + filename
    with open(current_dir + rel_path, "w") as f:
        f.write(render_template(filename, **args))

with app.app_context():
    for page in pages:
        args = pages[page]
        savefile(page, args)

app.run(debug=True)