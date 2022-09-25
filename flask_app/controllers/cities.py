from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import city

@app.route("/cities/new")
def new_city_form():
    return render_template("new_city.html")

@app.route("/cities/add_to_db", methods=["POST"])
def add_city_to_db():
    print("Before redirecting:")
    print(request.form) # Print the mayor of the city from the form
    data = {
        "name": request.form["name"],
        "mayor": request.form["mayor"],
        "population": request.form[ "population"]
    }
    city.City.create_city(data)
    # session["mayor"] = request.form["mayor"]
    # session["name"] = request.form["name"]
    # session["population"] = request.form["population"]
    # We'll later on add the data properly to the database
    # and not use session for this
    return redirect("/cities")

@app.route("/cities/<int:id>/show")
def show_city(id):
    data = {
        "id": id
    }
    return render_template("show_city.html", this_city = city.City.get_one_city(data))

@app.route('/cities')
def all_cities_page():
    return render_template("all_cities.html", all_cities= city.City.get_all_cities())

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route("/cities/<int:id>/edit")
def edit_page(id):
    data = {
        "id": id
    }
    return render_template("edit_city.html", this_city = city.City.get_one_city(data))

# Route that edits the city in the database
@app.route("/cities/<int:id>/edit_in_db", methods=["POST"])
def edit_city_in_db(id):
    data = {
        "name": request.form["name"],
        "mayor": request.form["mayor"],
        "population": request.form["population"],
        "id": id, # VERY IMPORTANT: Need the ID so we know which city we're editing
    }
    # Talk to model to add city to DB
    city.City.edit_city(data)
    return redirect(f"/cities/{id}/show") # Need an f-string to put the ID in

# Route that deletes a city from the database
@app.route("/cities/<int:id>/delete")
def delete_city(id):
    data = {
        "id": id,
    }
    city.City.delete_city(data)
    return redirect("/cities")