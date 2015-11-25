# import bs4
from bs4 import BeautifulSoup
import requests

page = requests.get("http://docs.python-requests.org/en/latest/user/quickstart/")
soup = BeautifulSoup(page.text, "html.parser")
# print (soup.body.prettify())
print(soup.body.findAll(['p', 'a', 'h1', 'h2', 'h3', 'h4', 'li']))  #, recursive=True))
# for incident in soup('td', class="jos_fabrik_icc_ccs_piracymap2012___narrations fabrik_element"):
#     break
#     where, linebreak, what = incident.contents[:3]
#     print where.strip()
#     print what.strip()
