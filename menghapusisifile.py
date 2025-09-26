#menghapus file
def clear_file(path):
    f = open(path,'w')
    f.close()

clear_file("scraping/test.txt")

#validasi extensi file
import os

def does_file_exist(path):
    return os.path.isfile(path)

print(does_file_exist("scraping/test.txt"))