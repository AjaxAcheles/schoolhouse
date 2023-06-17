from functools import wraps
from flask import render_template, session, redirect, url_for


def enter_password(original_function):
    @wraps(original_function)
    def decorated_function(*args, **kwargs):
        student_name = kwargs['student_name']
        if session.get(f"{student_name}_password_entered") is True:
            return original_function(*args, **kwargs)
        else:
            return redirect(url_for("enter_password",
                                    student_name=student_name))
    # return replacement function
    return decorated_function
