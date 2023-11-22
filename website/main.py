from flask import Flask, render_template, url_for, redirect, jsonify, request, session
from client import Client

EMAIL_KEY = 'email'
client = None

app = Flask(__name__)
app.secret_key = "thisisasecuritysecretkey"


def disconnect():
    """
    call this before the client disconnects from server
    :return:
    """
    global client
    if client:
        client.disconnect()


@app.route("/login", methods=["POST", "GET"])
def login():
    """
    displays main login page and handles saving email in session
    :exception POST
    :return: None
    """
    disconnect()
    if request.method == "POST":
        session[EMAIL_KEY] = request.form["email"]
        print(session)

        return redirect(url_for("home"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    """
    logs the user out by popping name from session
    :return: None
    """
    session.pop(EMAIL_KEY, None)
    return redirect(url_for("login"))


@app.route("/")
@app.route("/home")
def home():
    """
    displays home page if logged in
    :return: None
    """
    global client

    if EMAIL_KEY not in session:
        return redirect(url_for("login"))

    client = Client(session[EMAIL_KEY])

    return render_template("index.html")

@app.route("/run", methods=["GET"])
def send_message():
    """
    called from jQuery to send messages
    :return:
    """
    global client

    msg = request.args.get('msg')

    if client is not None:
        client.send_message(msg)
        return jsonify({
            "success": True,
            "msg": '',
            "data": []
        })

    return jsonify({
        "success":  False,
        "msg": 'Error',
        "data": []
    })


if __name__ == "__main__":
    app.run(debug=True)
