# import bs4
from bs4 import BeautifulSoup
#import json
_command = '<script type="meta/js" id="res"><script>'
soup = BeautifulSoup(_command, 'html.parser')

def parse_string_list_attr(v):
    if (v == None):
      return None
    return v

_json = []
for item in soup.find_all('script'):
    obj = {
      "id": item.get("id"), #.encode("utf-8"),
     # "command": item.get_text().strip(),
      "type": {
        'meta/js': "JS",
        'meta/sql': "SQL",
      }.get(item.get("type").encode("utf-8"), "UNKNOWN"),
    }

if item.has_attr("entity-id"): obj["entityId"] = long(item.get("entity-id"))
if item.has_attr("src"): obj["src"] = item.get("src")
if item.has_attr("db-alias"): obj["dbAlias"] = item.get("db-alias")
if item.has_attr("default"): obj["defaultValue"] = item.get("default")
if item.has_attr("help"): obj["help"] = item.get("help")
if item.has_attr("label"): obj["label"] = item.get("label")

obj["depends"] = parse_string_list_attr(item.get("depends"))
obj["states"] = parse_string_list_attr(item.get("states"))

_json.append(obj)

print (_json)
