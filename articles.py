from bs4 import BeautifulSoup
import requests

url = "https://www.nationalgeographic.com/science/"


def getArticles(amount):
    titles = []
    urls = []
    global url
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')

    table = soup.find_all('a', attrs={'class': 'AnchorLink PromoTile__Link'})
    i = 1
    for article in table:
        result = []
        for char in str(article).replace('<a aria-label="', ""):
            if char == ",":
                break
            else:
                result.append(char)

        title = ""
        for char in result:
            title += char
        titles.append(title)

        url_in_start = str(article).replace('<a aria-label="', "")
        for char in str(article).replace('<a aria-label="', ""):
            if char == ":":
                break
            else:
                url_in_start = url_in_start[1:]

        result = []
        for char in url_in_start:
            if char == '"':
                break
            else:
                result.append(char)

        new_url = ""
        for char in result:
            new_url += char

        new_url = new_url.replace("://", "")
        urls.append(new_url)

        if i == int(amount):
            break

    return titles, urls
