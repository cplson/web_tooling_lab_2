# Import Flask components for routing and rendering
from flask import flash
from flask import Blueprint, render_template, request, redirect, url_for
from models.student_model import add_student, get_all_students
import re


# Create a blueprint for the 'create' functionality
create_bp = Blueprint('create_student', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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

# Route to handle POST request from the Add modal form
@create_bp.route("/add_student", methods=["POST"])
def add_student_route():
    # Collect form data from the request
    student_data = {
        "name": request.form.get("name"),
        "email": request.form.get("email"),
        "program": request.form.get("program"),
        "enrollment_date": request.form.get("enrollment_date")
    }

    # Validate input data
    errors = validate_input(student_data)

    print('Image request in create controller: ', request.files.get("image"))
        #Handle image
    image_file = request.files.get("image")
    if image_file and image_file.filename != "":
        if not allowed_file(image_file.filename):
            errors.append("Invalid image format. Only png, jpg are allowed.")
    else:
        image_file = None

    # If errors, re-render page with error messages
    if errors:
        students = get_all_students()
        return render_template("index.html", students=students, errors=errors)

    # Add student to database
    print('Image file in create controller: ', image_file)
    add_student(student_data, image_file)
    flash("Student added successfully!","success" )
    # Redirect to main page after success
    return redirect(url_for("read_student.index"))

