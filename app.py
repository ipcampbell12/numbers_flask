from flask import Flask, request, flash, render_template
from datetime import datetime
import num_facts as nf


app = Flask(__name__)
app.secret_key = "fruity500"


# initialize database


@app.route("/number")
def index():
    flash("Enter a whole number to get some number facts")
    return render_template("index.html")


@app.route("/message", methods=["POST", "GET"])
def message():
    flash("Your number is " + str(request.form["num_input"]))
    flash(nf.get_digits(request.form["num_input"]))
    flash(nf.even_odd(request.form["num_input"]))
    flash(nf.prime_composite(request.form["num_input"]))
    flash(nf.squared(request.form["num_input"]))
    flash(nf.get_square_root(request.form["num_input"]))
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=5005, debug=True)
