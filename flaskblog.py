from flask import Flask, jsonify
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

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)