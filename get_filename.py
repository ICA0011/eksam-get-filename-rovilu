import requests
from bs4 import BeautifulSoup

URL = "http://upload.itcollege.ee/~aleksei/random_files/"


def get_filename(URL):
    elements = BeautifulSoup(requests.get(URL).text, "html.parser").find_all("a")
    count = 0
    for body in elements:
        filename = body.text
        if count == 10:
            return "http://upload.itcollege.ee/~aleksei/random_files//" + filename
        count += 1


if __name__ == "__main__":
    print("Element with index of 10 is " + get_filename(URL))
