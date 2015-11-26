#import bs4
from bs4 import BeautifulSoup
import requests

page = requests.get(
    "http://sankt-peterburg.tehnosila.ru/catalog/tehnika_dlya_kuhni/krupnaja_bytovaja_tehnika/holodilniki/-/27242")
soup = BeautifulSoup(page.text, "html.parser")
h1 = soup.body.findAll(['h1'])[0]
print(h1.text)

