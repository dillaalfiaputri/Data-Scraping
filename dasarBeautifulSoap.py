from bs4 import BeautifulSoup

html = "<div>This is a Div</div>"
soup = BeautifulSoup(html,"html.parser")

print(soup.div.text)

print("-------------------------")

from bs4 import BeautifulSoup

html = "<div>Ini adalah dokumen div</div><p>Ini adalah paragraf halaman luar.</p>"
soup = BeautifulSoup(html,"html.parser")

print(soup.p.text)

print("-------------------------")

from bs4 import BeautifulSoup

html = """
    <div>Ini adalah paragraf ke satu Div</div>
    <p>Ini adalah paragraf dengan sintag p</p>
    <div>Ini adalah paragraf ke dua Div</div>
"""
soup = BeautifulSoup(html,"html.parser")

print(soup)

print("-------------------------")

soup = BeautifulSoup(html,"html.parser")

print(soup)
print(soup.div)
print(soup.find_all("div"))
print(soup.find_all("div")[1])

print("-------------------------")

from bs4 import BeautifulSoup

html = """
    <div>Ini adalah paragraf ke satu Div</div>
    <p>Ini adalah paragraf dengan sintag p</p>
    <div class = 'bold'>Ini adalah paragraf ke dua Div</div>
"""
soup = BeautifulSoup(html,"html.parser")

print(soup.find_all("div",{'class':'bold'}))

print(soup.find_all("p",{'id':'para'}))

print("-------------------------")

from bs4 import BeautifulSoup

html = """
        <div id="d1" class="wide">
            <p id="p1">Ini Adalah Sintag Paragraf</p>
            <ing src=""/>
            <a id=a1"></a>
        </div>
        <div id="d2" class="small">
            <p id="p2">Ini Adalah Sintag Paragraf</p>
            <ing src=""/>
            <a id=a2"></a>
        </div>
"""

soup = BeautifulSoup(html,"html.parser")
print(soup.find_all('div',{'id':'d2'})[0].p)

print("-------------------------")

# soal 1
from bs4 import BeautifulSoup

html4 = """
        <div id='d1' class='wide'>
            <p id='p1'>This is a p</p>
            <div><p>OK</p></div>
            <img src=''/>
            <a id='a1'></a>
        <div id='d1' class='small'>
            <p id='p1'>This is a p</p>
            <div><p>KO</p></div>
            <img src=''/>
            <a id='a1'></a>
        </div>"""

soup = BeautifulSoup(html4,"html.parser")
print(soup.find_all("div", {'id':'d1'})[1].div.p.text) #1
print(soup.find_all("div", {'id':'d1', 'class':'small'})[0].div.p.text) #2

print("-------------------------")

# soal 2
from bs4 import BeautifulSoup

html4 = """<div>div1</div>
<div>div2</div>
<div>div3</div>
<div>div4</div>
<div>div5</div>
<div>div6</div>
<div>div7</div>
<div>div8</div>
<div>div9</div>
<div>div10</div>"""

soup = BeautifulSoup(html4, 'html.parser')
for index, div in enumerate(soup.find_all("div")):
    if (index + 1) % 2 == 0:
        print(div)