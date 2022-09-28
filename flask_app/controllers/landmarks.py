from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import landmark, city

@app.route('/all_landmakrs')
def new_landmark_page():
    return render_template("add_landmark.html", all_cities =city.City.get_all_cities())

#route that shows the form for adding a landmark
@app.route('landmarks/new')
def new_landmark_page():
    return render_template("add_landmark.html", all_cities =city.City.get_all_cities())

#route to add a land mark
@app.route("/landmarks/add_to_db", methods=['post'])
def add_landmark_to_db():
    data = {
        "name": request.form["name"],
        "year_created": request.form["year_created"],
        "address": request.form[ "address"],
        "city_id": request.form[ "city_id"]
    }
    landmark.Landmark.add_landmark(data)
    return redirect("/landmarks")