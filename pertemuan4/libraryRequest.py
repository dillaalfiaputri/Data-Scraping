import requests
import os
from bs4 import BeautifulSoup
import pythonhandling

# result = requests.get("https://www.detik.com/")

# print(result)

# import requests

# result = requests.get("https://www.detik.com/")
# print(result)
# print(result.encoding)
# print(result.status_code)
# print(result.elapsed)
# print(result.url)
# print(result.history)
# print(result.headers['Content-Type'])


# def create_directory(pythonhandling):
#     if not os.path.exists(pythonhandling):
#         os.mkdir(pythonhandling)

# def main_scraper(url, directory):
#     create_directory(directory)
    
#     source_code = requests.get(url)
#     source_text = source_code.text
#     print(source_text)

# main_scraper("https://example.com", "hasil_scraping")

import requests
import os
from bs4 import BeautifulSoup

def create_directory(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)

def main_scraper(url, directory):
    create_directory(directory)
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text, "html.parser")
    results = soup.find_all("div", attrs={"class": "grid-row list-content list-content--column"})
    
    print(f"Ditemukan {len(results)} elemen")
    for item in results:
        print(item)

main_scraper("https://www.detik.com/", "Hasil")

# <div class="grid-row list-content list-content--column">