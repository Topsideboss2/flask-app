from flask import Blueprint, url_for, jsonify, redirect

api = Blueprint("api", __name__)

# json
@api.route("/")
@api.route("/home")
def api_home():
    return jsonify({"message": "Hello, World!"})

# variable
@api.route("/<name>")
def api_name(name):
    return jsonify({"message": f"Hello, {name}!"})

# redirect
@api.route("/admin")
def api_admin():
    return redirect(url_for("api_name", name="Admin!"))