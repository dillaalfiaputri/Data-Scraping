def create_new_file(path):
    f= open(path,'w')
    f.write("")
    f.close()

def write_to_file(path,data):
    with open(path,'a') as file:
        file.write(data + '\n')

def read_data(path):
    with open(path,'rt') as file:
        for line in file:
            print(line)

create_new_file("scraping/file.txt")
write_to_file("scraping/file.txt","This is a line")
write_to_file("scraping/file.txt","This is a line")

read_data("scraping/file.txt")