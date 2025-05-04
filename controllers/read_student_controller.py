from flask import Blueprint, render_template, Response
from bson import ObjectId
from models.student_model import get_all_students, db
import gridfs

fs =gridfs.GridFS(db)

read_bp = Blueprint("read_student", __name__)

@read_bp.route("/")
def index():
    students = get_all_students()
    return render_template("index.html", students=students)

@read_bp.route("/image/<image_id>")
def save_image(image_id):
    try:
        image_file = fs.get(ObjectId(image_id))
        return Response(image_file.read(), mimetype=image_file.content_type)
    except:
        return "Image not found", 404