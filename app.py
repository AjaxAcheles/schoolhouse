from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    abort,
    session
)
from db_functions import *
from decorators import *
from passwords import *
from os import getcwd, listdir, walk, scandir
from glob import glob
app = Flask(__name__)
app.secret_key = "╚£æ@}65☺1∟48¿↑[15]1φ516û jkhe5/▌84Ü651J65♠"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/courses")
def courses():
    return render_template("courses.html")


@app.route('/math')
def math():
    return render_template("math.html")


@app.route('/python')
def python():
    return render_template("python.html")


@app.route('/web_dev')
def web_dev():
    return render_template("web_dev.html")


@app.route('/students', methods=["GET", "POST"])
def students():
    if request.method == "GET":
        student_names = get_student_names()

        # debug ############################################   DEBUG DEBUG DEBUG DEBUG   ########################
        for student in session:
            session[student] = False

        if student_names is None:
            abort(404)

        # checks to see if the student has a password on their projects
        is_locked = {}
        for student in student_names:
            if get_password(student) is None:
                is_locked[student] = False
            else:
                is_locked[student] = True
        print(is_locked)

        return render_template("students.html",
                               students=student_names,
                               is_locked=is_locked)
    
    if request.method == "POST":
        student_name = request.form["student"]
        return redirect(url_for("student_projects",
                                student_name=student_name))


@app.route('/students/<student_name>/projects', methods=["GET", "POST"])
@enter_password
def student_projects(student_name):
    if request.method == "GET":
        student_projects = find_student_projects(student_name)
        if student_projects is None:
            abort(404)
        return render_template("projects.html",
                               projects=student_projects)
    if request.method == "POST":
        project_name = request.form["project"]
        return redirect(url_for("open_project_folder",
                                student_name=student_name,
                                project_name=project_name))


@app.route('/students/<student_name>/projects/<project_name>', methods=["GET", "POST"])
@enter_password
def open_project_folder(student_name, project_name):
    if request.method == "GET":
        project_folder_contents = get_project_folder_contents(student_name, project_name)
        if project_folder_contents is None:
            abort(404)
        folder_path = get_project_folder_contents(student_name, project_name, get_path=True)
        return render_template("open_project.html",
                               student_name=student_name,
                               project_name=project_name,
                               project_folder_contents=project_folder_contents,
                               folder_path=folder_path)
    
    if request.method == "POST":
        file_name = request.form["file-name"]
        return redirect(url_for("run_file",
                                student_name=student_name,
                                project_name=project_name,
                                file_name=file_name))

@app.route("/students/<student_name>/projects/<project_name>/<file_name>", methods=["GET", "POST"])
@enter_password
def run_file(student_name, project_name, file_name):
    if request.method == "GET":
        file_contents = get_file_contents(student_name=student_name, project_name=project_name, file_name=file_name)
        return file_contents
    
    if request.method == "POST":
        return "post successful"

@app.route("/students/<student_name>/enter_password", methods=["GET", "POST"])
def enter_password(student_name):
    if request.method == "GET":
        if get_password(student_name) is None:
            session[f"{student_name}_password_entered"] = True
        if session.get(f"{student_name}_password_entered") is True:
            return redirect(url_for("student_projects",
                                    student_name=student_name))
        return render_template("enter_password.html",
                               student_name=student_name)
    if request.method == "POST":
        entered_password = request.form["password"]
        password = get_password(student_name)
        if entered_password == password:
            session[f"{student_name}_password_entered"] = True
        return redirect(url_for("student_projects",
                                student_name=student_name))

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")


if __name__ == "__main__":
    # remove if statement after done coding the website.
    app.run(debug=True)
