import requests
from bs4 import BeautifulSoup


def check(url):
    try:
        response = requests.get(url)
        return True
    except:
        return False


##############################################################
def check_lang(url):
    try:
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html.parser')
        print(soup.html["lang"])
        lang = soup.html["lang"]
        return lang
    except:
        return "Not Found"
