import os

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def does_file_exist(path):
    return os.path.exists(path)

def create_new_file(path):
    open(path, "w", encoding="utf-8").close()

def write_to_file(path, text):
    with open(path, "a", encoding="utf-8") as f:
        f.write(text)

def get_details(url):
    print("Detail:", url)
