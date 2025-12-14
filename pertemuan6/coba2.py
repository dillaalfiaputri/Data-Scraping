from bs4 import BeautifulSoup
import requests
import os
import scraping

def main_scraper(url, directory):
    scraping.create_directory(directory)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("a", href=True)

    file_path = os.path.join(directory, "artikel.txt")

    if not scraping.does_file_exist(file_path):
        scraping.create_new_file(file_path)

    for article in articles:
        link = article.get("href")
        if link.startswith("http"):
            data = f"URL: {link}\n"
            scraping.write_to_file(file_path, data)
            print(data)

main_scraper("https://tekno.kompas.com", "berita_kompas")
