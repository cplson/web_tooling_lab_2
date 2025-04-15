from flask import Blueprint, render_template

from models.student_model import get_all_students

read_bp = Blueprint("read_student", __name__)

@read_bp.route("/")
def index():
    students = get_all_students()
    return render_template("index.html", students=students)