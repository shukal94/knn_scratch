import os


def make_executable(path):
    os.system('chmod 777 {}'.format(path))


def execute_bash_script(path):
    make_executable(path)
    os.system('sh {}'.format(path))
