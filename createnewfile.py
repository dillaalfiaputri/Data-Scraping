def create_new_file(path):
    f=open(path,'w')
    f.write("")
    f.close()

create_new_file("scraping/test.txt")

def write_to_file(path,data):
    with open(path,'a') as file:
        file.write(data + '\n')