from flask import session
passwords = {
    "jonah": "4507",
    "chaz": None,
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
