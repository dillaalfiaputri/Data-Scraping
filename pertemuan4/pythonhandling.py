import os

def ucapan(text):
    print(text)

ucapan("Haii")

def create_directory(datascraping):
    if not os.path.exists(datascraping):
        os.mkdir(datascraping)

create_directory("scraping")