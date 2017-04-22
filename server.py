from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

jobs= ["Software-Engineer", "QA-Engineer", "Product-Manager"]

# YOUR ROUTES GO HERE
@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/application-form')
def application_form():
    return render_template("application-form.html", jobs=jobs)

@app.route('/application-success', methods=["POST"])
def show_application ():
    fname=request.form.get("firstname")
    lname=request.form.get("lastname")
    salary=request.form.get("salary")
    jobtitle=request.form.get("jobtitle")
    jobtitle=jobtitle.replace("-", " ")

    return render_template("application-response.html",
                           fname=fname, 
                           lname=lname,
                           salary=salary,
                           jobtitle=jobtitle)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
