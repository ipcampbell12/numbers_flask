from flask import Flask, request, flash, render_template, session
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
    number = str(request.form["num_input"])

    if request.form["submit"] == 'Get facts':
        if number.isnumeric() != True:
            flash("Silly goose! Your number must be a positive integer!")
        else:
            flash("Your number is " + str(request.form["num_input"]))
            flash(nf.get_digits(request.form["num_input"]))
            flash(nf.even_odd(request.form["num_input"]))
            flash(nf.prime_composite(request.form["num_input"]))
            flash(nf.squared(request.form["num_input"]))
            flash(nf.get_square_root(request.form["num_input"]))
    if request.form["submit"]=='Clear Output':
            session['_flashes'].clear()
    return render_template("index.html")

    

if __name__ == "__main__":
    app.run(port=5005, debug=True)
