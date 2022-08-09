from bs4 import BeautifulSoup
import requests
from getpass import getpass
url = "https://view.sy/self-care/#/usage"

r = requests.get(url, auth=('email', getpass()))

# soup = BeautifulSoup(r.text, features='html.parser')
# print(soup)

print(r.headers)
print(r.text)
