# # halaman 1 j
# from selenium import webdriver
# from bs4 import BeautifulSoup

# url = "https://tekno.kompas.com/gadget"

# driver = webdriver.Chrome()
# driver.get(url)                   

# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')

# data = soup.find_all("div", class_="latest--news mt2 clearfix")  

# print(data)

# driver.quit()

# halaman 1 s
# from selenium import webdriver
# from bs4 import BeautifulSoup
# import fungsi
# import requests
# import os

# def main_scraper(url):
#     headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'}
#     driver = webdriver.Chrome()
#     # driver.set_page_load_timeout(5000)
#     full_url = f"{url}"
#     driver.get(full_url)
#     html = driver.page_source
#     soup = BeautifulSoup('html', 'html.parser')
#     hasil = soup.find_all("div", class_='latest--news mt2 clearfix')
    
#     for i in range(len(hasil)):
#         Card = hasil[i].find("div", {'class':'article__list clearfix'})
#         Judul = hasil[i].find("a", {'class':'article__link'})
#         if Card and Judul:
#             print("Card : " + Card.text)
#             print("Judul : " + Judul.text)
#             print("=====================================")

#     fungsi.create_directory('hasil')
#     file_path = os.path.join('hasil', 'kompasparser.txt')
#     fungsi.write_to_file(file_path, 'html')
#     # print(html)

# main_scraper("https://tekno.kompas.com/gadget")

# # halaman 2
# import fungsi
# import requests
# from bs4 import BeautifulSoup

# def main_scraper(url):
#     source_code = requests.get(url)
#     source_text = source_code.text
#     soup = BeautifulSoup(source_text, "html.parser")
#     articles = soup.find_all("article", {'class': 'post'})
    
#     for article in articles:
#         article_format = "URL : " + article.a.get("href") + "\n" + "Judul : " + article.getText() + "\n"
#         print(article_format)

# main_scraper("https://tekno.kompas.com/")

# # halaman 1 r
# from selenium import webdriver
# from bs4 import BeautifulSoup
# import fungsi
# import requests
# import os
# import time

# def main_scraper(url):

#     driver = webdriver.Chrome()
#     driver.set_page_load_timeout(5000)
#     driver.get(url)

#     # tunggu javascript load
#     time.sleep(2)

#     html = driver.page_source
#     soup = BeautifulSoup(html, "html.parser")

#     # selector yang benar
#     hasil = soup.find_all("article", class_="latest--news mt2 clearfix")

#     for item in hasil:
#         Card = item.find("div", {'class':'article__list clearfix'})
#         Judul = item.find("a", {'class':'article__link'})
        
#         if Card and Judul:
#             print("Card  : ", Card.text.strip())
#             print("Judul : ", Judul.text.strip())
#             print("=====================================")

#     # simpan file
#     fungsi.create_directory('hasil')
#     file_path = os.path.join('hasil', 'kompasparser.txt')
#     fungsi.write_to_file(file_path, html)

#     driver.quit()


# main_scraper("https://tekno.kompas.com/gadget")

import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time

url = "https://tekno.kompas.com/gadget"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
html_asli = response.text

driver = webdriver.Chrome()
driver.get(url)

time.sleep(3)  

html_selenium = driver.page_source
driver.quit()

with open("gabungan_kompas.txt", "w", encoding="utf-8") as f:
    f.write("===== HTML ASLI (VIEW PAGE SOURCE) =====\n\n")
    f.write(html_asli)
    f.write("\n\n\n\n=========================================\n")
    f.write("===== HTML SELENIUM (DOM RENDER) =====\n\n")
    f.write(html_selenium)

print("BERHASIL! File gabungan_kompas.txt telah dibuat.")
