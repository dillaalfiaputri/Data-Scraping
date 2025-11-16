import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def does_file_exist(filepath):
    return os.path.exists(filepath)

def create_new_file(filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        pass

def write_to_file(filepath, content):
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(content + "\n")
