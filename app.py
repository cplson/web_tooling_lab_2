from flask import Flask, render_template
from controllers.create_student_controller import create_bp
from controllers.read_student_controller import read_bp
from controllers.update_student_controller import update_bp
from controllers.delete_student_controller import delete_bp

# initialize flask web app
app = Flask(__name__)

app.register_blueprint(create_bp)
app.register_blueprint(read_bp)
app.register_blueprint(update_bp)
app.register_blueprint(delete_bp)

# required for flashing messages
app.secret_key="your-secret-key"

if __name__ == "__main__":
    app.run(debug=True)