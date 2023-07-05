from flask import session
passwords = {
    "chaz": "ILikeCoding1",
    "aiden": None,
    "micah": None
}


def get_password(student_name):
    password = passwords[student_name]
    return password

def is_unlocked(student_name):
    if session.get(f"{student_name}_password_entered") is True:
        return True
    else:
        return False
