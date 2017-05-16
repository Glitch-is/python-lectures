from flask import Flask, url_for, request, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to my site"

@app.route("/profile/<int:userid>")
def search(userid):
    users = ["konni", "hlynur", "other"]
    return f"Hello {users[userid]}!"

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        return str(request.args)
    return render_template("login.html")

@app.route("/admin")
def admin():
    return url_for('login')

