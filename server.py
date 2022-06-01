

from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Hello let's learn about classic monsters"

if __name__ == "main":
    app.run(debug=True)
