from plistlib import load
from flask import Flask, request, flash, render_template, session, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import num_facts as nf


app = Flask(__name__)
app.secret_key = "fruity500"


# points to where it is located
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///number.db'
db = SQLAlchemy(app)


# this is my Number model
class Number(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    #returns a string when a new number is created with the id 
    def __repr__(self):
        return '<Number %r>' % self.id



#loads the index.html page
@app.route("/number",methods=["POST", "GET"])
def index():
    return render_template("index.html")



#flashes info about the number and clears the input
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
            number_content = request.form['num_input'] or None
            new_number = Number(number = number_content)
            if request.method == 'POST':
                try:
                    db.session.add(new_number)
                    db.session.commit()
                    return redirect("/number")
                except:
                    return "There was an issue adding your number"
            else: 
                numbers = Number.query.order_by(Number.date_created).all()
    if request.form["submit"]=='Clear Output':
            session['_flashes'].clear()
    return render_template("index.html")

""" @app.route("/number",methods=['POST',"GET"])
def load_number():
    number_content = request.form['num_input'] or None
    new_number = Number(number = number_content)
    if request.method == 'POST':
        try:
            db.session.add(new_number)
            db.session.commit()
            return redirect("/number")
        except:
            return "There was an issue adding your number"
    else: 
        numbers = Number.query.order_by(Number.date_created).all()
        return render_template('index.html', numbers=numbers) """


if __name__ == "__main__":
    app.run(port=5005, debug=True)

