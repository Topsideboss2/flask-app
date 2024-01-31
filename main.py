from flask import Flask, jsonify, redirect, url_for, render_template
# proxy fix
from werkzeug.middleware.proxy_fix import ProxyFix
from blog.blog import blog
from api.api import api

# app
app = Flask(__name__)

# blueprint
app.register_blueprint(blog, url_prefix="/blog")
app.register_blueprint(api, url_prefix="/api")

# proxy fix
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1, x_prefix=1, x_for=1)

# string
@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<name>")
def error(name):
    if name == "about":
        return render_template("about.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/generic")
def generic():
    return render_template("generic.html")

@app.route("/elements")
def elements():
    return render_template("elements.html")
    
@app.route("/cv/download")
def cv():
    return redirect('https://drive.google.com/file/d/15-CZldT1guNk8AHrtVfJCwVZDZMKx3Gc/view?usp=sharing')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)