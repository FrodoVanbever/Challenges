from flask import Flask
from flask import render_template

import datetime

microweb_app = Flask(__name__)

@microweb_app.route("/")
def main():
    return render_template("index.html")

@microweb_app.route("/date")
def date():
    return render_template("date.html" , date_now = datetime.datetime.now())

@microweb_app.route("/ip")
def ip():
    return render_template("ip.html" , date_now = datetime.datetime.now())

if __name__ == "__main__":
    microweb_app.run(host="0.0.0.0", port=5050)