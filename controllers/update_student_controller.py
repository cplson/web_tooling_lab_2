# from tkinter import image_names

from flask import Blueprint, request, redirect, url_for, render_template, flash

# from controllers.create_student_controller import allowed_file
from models.student_model import update_student, get_all_students
import re

# Create blueprint for update
update_bp = Blueprint('update_student', __name__)


# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

#Input validation function
def validate_input(data):
    errors = []
    if not  data.get("name") or not re.match(r'^[A-Za-z ]+$', data["name"]):
        errors.append("Name must only contain letters and spaces.")
    if not  data.get("email") or not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', data['email']):
        errors.append("Invalid email address.")
    if not data.get("program") or not re.match(r'^[A-Za-z0-9 ]+$', data["program"]):
        errors.append("Program must be alphanumeric")
    if not data.get("enrollment_date") or re.match(r'\b\d{4}-\d{2}-\d{2}\b', data["enrollment_date"]):
        errors.append("Must be valid date of format 'YYYY-MM-DD'.")
    return  errors


# Route to update student by ID
@update_bp.route("/update/<id>", methods=["POST"])
def update_student_route(id):
    # Extract form data
    update_data = {
        "name": request.form.get("name"),
        "email": request.form.get("email"),
        "program": request.form.get("program"),
        "enrollment_date": request.form.get("enrollment_date")
    }

    print(id, update_data)
    # Validate input
    errors = validate_input(update_data)

    # #Handle image
    # image_file = request.files.get("image")
    # if image_file and image_file.filename != "":
    #     if not allowed_file(image_file.filename):
    #         errors.append("Invalid image format. Only png, jpg are allowed.")
    # else:
    #     image_file = None

    # If validation fails, return to form with errors
    if errors:
        print('there are errors')
        print(errors)
        students = get_all_students()
        update_data["_id"] = id
        return render_template("index.html", students=students, errors=errors, student=update_data)

    update_student(id, update_data)
    flash("Student updated successfully!","success" )
    return redirect(url_for("read_student.index"))
