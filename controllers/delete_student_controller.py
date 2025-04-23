
from flask import blueprints, request, redirect, url_for, Blueprint
from models.student_model import delete_student

# Create blueprint for delete functionality
delete_bp = Blueprint('delete_student', __name__)

# Route to delete student by ID
@delete_bp.route("/delete/<id>", methods=["POST"])
def delete_student_route(id):
    delete_student(id) # Perform DB deletion

    return redirect(url_for("read_student.index")) # Redirect to homepage