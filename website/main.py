from flask import Flask, render_template, url_for, redirect, request, session
from client import Client

EMAIL_KEY = 'email'

app = Flask(__name__)
app.secret_key = "thisisasecuritysecretkey"


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        print('POST')
        session[EMAIL_KEY] = request.form["email"]
        print(session)

        return redirect(url_for("home"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop(EMAIL_KEY, None)
    return redirect(url_for("login"))


@app.route("/")
@app.route("/home")
def home():
    if EMAIL_KEY not in session:
        return redirect(url_for("login"))

    return render_template("index.html")

@app.route("/run", methods=["GET"])
def run():
    msg = request.args.get('msg')
    print(msg)
    return "test"


if __name__ == "__main__":
    app.run(debug=True)
