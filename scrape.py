import os
from bs4 import BeautifulSoup
import requests

response = requests.get(os.environ["url"])
soup = BeautifulSoup(response.text, 'html.parser')

print(soup.title)
