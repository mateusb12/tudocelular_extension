import bs4
from bs4 import BeautifulSoup
import requests


def get_name() -> str:
    brute_name = soup.find("div", id="fwide_column")
    possible_names = []
    raw_name = ""
    for i in brute_name.contents:
        if isinstance(i, bs4.element.Tag):
            possible_names.append(i.text)

    if "\n" in possible_names[0]:
        raw_name = possible_names[1]
    else:
        raw_name = possible_names[0]

    item_list = ("<h2>", "<strong>", "</strong>", "</h2>", "<small>", "</small>")

    for r in item_list:
        raw_name = raw_name.replace(r, "")

    return raw_name


def get_image() -> str:
    return soup.find("aside", class_="narrow_column").contents[1].attrs["src"]


def get_price() -> str:
    price_options = soup.find("div", class_="compras_items").contents[1]
    price_tag = None
    for price in price_options:
        if isinstance(price, bs4.element.Tag):
            if price.attrs["class"] == ["shop_places"]:
                price_tag = price

    price_link = None
    for link in price_tag:
        if isinstance(link, bs4.element.Tag):
            if link.attrs["class"] == ["price"]:
                price_link = link

    return price_link.contents[1].text


smartphone_id = "Motorola/fichas-tecnicas/n6693/Motorola-Moto-E7-Power.html"

base_id = "https://www.tudocelular.com/"
final_id = base_id + smartphone_id

html = requests.get(final_id).content
soup = BeautifulSoup(html, 'html.parser')

smartphone_dict = {"name": get_name(), "image": get_image(), "price": get_price()}

print(smartphone_dict)
