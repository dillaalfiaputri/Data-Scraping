# #melakukan uji coba scrape page 1
# import requests
# from bs4 import BeautifulSoup

# html_doc = requests.get("https://www.detik.com/jatim/berita/indeks")

# soup = BeautifulSoup(html_doc.text, 'html.parser' )

# #page 2
# import requests
# from bs4 import BeautifulSoup

# html_doc = requests.get("https://www.detik.com/jatim/berita/indeks")

# soup = BeautifulSoup(html_doc.text, 'html.parser' )

# populer_area = soup. find(attrs={'class': 'grid-row list-content'})

# titles = populer_area. findAll(attrs={'class': 'media __ title'})
# images = populer_area. findAll(attrs={'class': 'media __ image' })

# for image in images:
#     print(image.find('a').find('img'))

# #page 3
# import requests
# from bs4 import BeautifulSoup

# html_doc = requests.get("https://www.detik.com/jatim/berita/indeks")

# soup = BeautifulSoup(html_doc.text, 'html.parser' )

# populer_area = soup. find(attrs={'class': 'grid-row list-content' })

# texts = populer_area. findAll(attrs={'class':'media__text' })
# images = populer_area. findAll(attrs={'class':'list-content__item'})

# for image in images:
#     print(image.find('div',{'class':'media __ date'}).find('span' ) ['title' ])

# #via coba
import requests
from bs4 import BeautifulSoup

html_doc = requests.get("https://www.detik.com/jatim/berita/indeks")

soup= BeautifulSoup(html_doc.text,'html.parser')

populer_area = soup.find(attrs={'class':'grid-row list-content'})

titles= populer_area.findAll(attrs={'class':'media__text'})
images= populer_area.findAll(attrs={'class':'media__image'})

for image in images:
    print(image.find('a').find('img')['title'])