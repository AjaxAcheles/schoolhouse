def get_student_names():
    from os import listdir, getcwd
    # open and retrieve data from json file
    path = getcwd()
    students_names = listdir(path + "\\templates\\students_code")
    # get the students names
    if students_names:
        return students_names
    # if students not found, then return none
    return None


def find_student_projects(target_student):
    from os import listdir, getcwd
    # open and retrieve data from files
    path = getcwd()
    students_names = listdir(path + "\\templates\\students_code")
    if students_names:
        for student_name in students_names:
            if student_name == target_student:
                # get the student's projects
                try:
                    student_projects = listdir(path + f"\\templates\\students_code\\{student_name}\\projects")
                    # return the student's projects if found
                    return student_projects
                except:
                    return None
    # if student not found, then return none
    return None


def get_project_path(student_name, project_name, file_name, get_local_path:bool=True):
    from os import getcwd, path as os_path
    # open and retrieve data from files
    path = getcwd()
    local_path = f"students_code\\{student_name}\\projects\\{project_name}\\{file_name}"
    project_path = path + "\\templates\\" + local_path
    if os_path.isfile(project_path):
        if get_local_path is True:
            return local_path
        elif get_local_path is False:
            return project_path
    return None


def get_project_folder_contents(student_name, project_name, get_path:bool=False):
    from os import getcwd, listdir
    # open and retrieve data from files
    path = getcwd()
    local_path = f"students_code\\{student_name}\\projects\\{project_name}"
    project_path = path + "\\templates\\" + local_path
    if get_path is False:
        if listdir(project_path):
            return listdir(project_path)
    elif get_path is True:
        return project_path
    return None

def get_file_contents(student_name, project_name, file_name):
    from os import getcwd
    # open and retrieve data from files
    path = getcwd()
    local_path = f"students_code\\{student_name}\\projects\\{project_name}\\{file_name}"
    file_path = path + "\\templates\\" + local_path
    # reads the file contents
    file_obj = open(file_path)
    file_contents = file_obj.read()
    file_obj.close()
    return file_contents
