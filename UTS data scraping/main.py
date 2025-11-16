import requests
from bs4 import BeautifulSoup
import os
import fungsi

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_details(url):
    try:
        response = requests.get(url)
        source_text = response.text
        soup = BeautifulSoup(source_text, "html.parser")

        title_tag = soup.find("h1", {'class': 'read__title'})
        divEntry = soup.find("div", {'class': 'read__content'})

        title = title_tag.text.strip() if title_tag else ""
        content = ""
        if divEntry:
            paragraf = divEntry.find_all("p")
            content = "\n".join(p.text.strip() for p in paragraf if p.text.strip())

        if content.strip():
            print("Judul :", title)
            print("URL   :", url)
            print("Isi Berita :")
            print(content)
            print("================================================")

            hasil_path = os.path.join(BASE_DIR, "cerita.doc")
            fungsi.write_to_file(hasil_path, f"Judul : {title}")
            fungsi.write_to_file(hasil_path, f"URL   : {url}")
            fungsi.write_to_file(hasil_path, f"Isi Berita :\n{content}")
            fungsi.write_to_file(hasil_path, "================================================")
    except Exception as e:
        print(f"Error getting details: {e}")

def main_scraper(url, directory):
    fungsi.create_directory(directory)
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text, "html.parser")

    articles = soup.find_all("h3", {'class': 'article__title'})

    for article in articles:
        a_tag = article.find("a")
        if a_tag:
            link = a_tag.get("href")
            if link.startswith("/"):
                link = "https://www.kompas.com" + link

            get_details(link)

main_scraper("https://www.kompas.com/tekno/gadget", "Kompas News")

# def get_details(url):
#     source_code = requests.get(url)
#     source_text = source_code.text
#     soup = BeautifulSoup(source_text, "html.parser")
#     divEntry = soup.find("article", {'class':'post'})
#     soup = BeautifulSoup(str(divEntry), "html.parser")
#     paragraf = soup.find_all("p")
#     write_to_file("Carpan Islami/artikel.doc", "Paragraf: \n")
#     for p in paragraf:
#         write_to_file("Carpan Islami/artikel.doc", p.text)
#     print("------------------------------------------------")
#     write_to_file("Carpan Islami/artikel.doc", "================================================")
