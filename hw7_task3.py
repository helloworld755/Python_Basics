import os
import my_project
import templates
import shutil

root_dir = my_project.__path__[0]
destin_dir = templates.__path__[0]
for root, dirs, files in os.walk(root_dir):
    for d in dirs:
        if d == 'templates':
            tem_root = os.path.join(root, d)
            for root2, dirs2, files2 in os.walk(tem_root):
                for d2 in dirs2:
                    shutil.copytree(os.path.join(root2, d2), destin_dir + '\\' + d2)
            for f in files:
                shutil.copy2(os.path.join(root, f), destin_dir)
