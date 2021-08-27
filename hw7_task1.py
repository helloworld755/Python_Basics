import os

project_name = 'my_project_' + input('Project name: ')
starter_config = ['settings', 'mainapp', 'adminapp', 'authapp']
if not os.path.exists(project_name):
    os.mkdir(project_name)
    for el in starter_config:
        dir_path = os.path.join(project_name, el)
        os.mkdir(dir_path)
