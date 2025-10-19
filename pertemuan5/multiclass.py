# COBA 1
from bs4 import BeautifulSoup
soup = BeautifulSoup('<html><body><div class = "class1">''</div><div class="class2"></div><div class="class3"></div></body></html>')
soup.findAll(True, {"class":{"class1", "class2"}})

# COBA 2
from bs4 import BeautifulSoup
import os
import fungsi
import requests

def main_scraper(url,directory):
    fungsi.create_directory(directory)
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text,"html.parser")
    articles = soup.find_all("h3", {'class':"article__title"})
    articles2 = soup.find_all(True, {'class':['article_box','article_title']})

    for article in articles:
        print("URL :"+ article.a.get("href"))
        print("Judul: "+ article.text)
        print()
    for article2 in articles2:
        print("URL2:"+article2.a.get("href")) 
        print("Judul2 :"+ article2.text)
        print()

main_scraper('https://tekno.kompas.com/gadget', 'hasil')


# COBA 3
from bs4 import BeautifulSoup
import fungsi
import requests

def main_scraper(url, directory):
    fungsi.create_directory(directory) #Membuat Directory
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text,"html.parser")
    articles = soup. find_all("h2", {'class':'entry-title'})

    for article in articles:
        print("URL : " + article.a.get("href"))
        print("Judul : " + article.text)
        print()
        article_format = "URL : " + article.a.get("href") + "\n" + "title : " + article.a.text + "\n"

        if fungsi.does_file_exist(directory + "/artikel.txt") is False:
            fungsi.create_new_file(directory + "/artikel.txt")

        fungsi.write_to_file(directory + "/artikel.txt", article_format)
        print(article_format)
main_scraper("https://dongengceritarakyat.com/category/cerita-anak/","Hasil")


# TUGASS
from bs4 import BeautifulSoup
import os
import fungsi
import requests
import re

def main_scraper(url, directory):
    fungsi.create_directory(directory)
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text, "html.parser")

    articles = soup.find_all("h3", {'class': "article__title"})
    articles2 = soup.find_all(True, {'class': ['article_box', 'article_title']})

    def extract_date(article_url):
        match = re.search(r'/(\d{4}/\d{2}/\d{2})/', article_url)
        if match:
            return match.group(1)
        return "Tanggal tidak ditemukan"

    for article in articles:
        url_artikel = article.a.get("href")
        print("URL: " + url_artikel)
        print("Tanggal: " + extract_date(url_artikel))
        print("Judul: " + article.text)
        print()

    for article2 in articles2:
        url_artikel2 = article2.a.get("href")
        print("URL2: " + url_artikel2)
        print("Tanggal2: " + extract_date(url_artikel2))
        print("Judul2: " + article2.text)
        print()

main_scraper('https://tekno.kompas.com/gadget', 'hasil')