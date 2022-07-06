import subprocess
import os

def run_python(code,problem_id):

    
    file_name = 'code.py'
    file = open(file_name, 'w')
    file.write(code)
    file.close()

    
    process = subprocess.Popen(['python', file_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    os.remove(file_name)

    
    return stdout.decode('utf-8')

def run_code(code, language, problem_id, user_id):
    if language == 'C':
        return run_c(code, problem_id, user_id)
    elif language == 'C++':
        return run_cpp(code, problem_id, user_id)
    elif language == 'python':
        return run_python(code, problem_id)
    elif language == 'JavaScript':
        return run_javascript(code, problem_id, user_id)
