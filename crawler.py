import requests
import os
from bs4 import BeautifulSoup

if os.path.exists("urls.txt"):
    os.remove("urls.txt")

tracker = 0
url = "https://marketingtochina.com/blog/"
f = open("urls.txt", "a")

def crawl(url):
    soup = BeautifulSoup(requests.get(url).text, "html.parser")

    for link in soup.find_all('a'):
        if "rel" in link.attrs and link.attrs['rel'] == ['bookmark']:
            global tracker
            tracker += 1
            f.write(link.get("href") + "\n")
            print(f"{tracker}: {link.get('href')}")

        elif 'class' in link.attrs and link.attrs["class"] == ['next', 'page-numbers']:
            print("NEXT PAGE")
            crawl(link.get("href"))


crawl("https://marketingtochina.com/blog/")
f.close()
print(f"Returned {tracker} urls.")