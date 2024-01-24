from flask import Flask, jsonify, redirect, url_for
# proxy fix
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

# proxy fix
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1, x_prefix=1, x_for=1)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hello")
def api():
    return jsonify({"message": "Hello, World!"})

@app.route("/hello/<name>")
def api_name(name):
    return jsonify({"message": f"Hello, {name}!"})

@app.route("/hello/admin")
def api_admin():
    return redirect(url_for("api_name", name="Admin!"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)