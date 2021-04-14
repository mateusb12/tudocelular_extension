from typing import List

import bs4
from bs4 import BeautifulSoup
import requests


# smartphone_id = "Motorola/fichas-tecnicas/n6693/Motorola-Moto-E7-Power.html"

# final_id = base_id + smartphone_id


def get_phonelist_from_single_page(page_id: str) -> List[str]:
    html = requests.get(page_id).content
    soup = BeautifulSoup(html, 'html.parser')
    smartphone_ids = []
    list_body = soup.find("div", id="cellphones_list")

    for smartphone in list_body.children:
        if type(smartphone) != bs4.element.NavigableString:
            phone_pic = smartphone.find("a", class_="pic")
            if phone_pic:
                smartphone_link = phone_pic.attrs["href"]
                if smartphone_link:
                    smartphone_ids.append("https://www.tudocelular.com" + smartphone_link)

    return smartphone_ids


def generate_page_links() -> List[str]:
    multiple_pages_links = []
    sequence = ["", "_2", "_3", "_4", "_5"]

    for i in sequence:
        current_link = "https://www.tudocelular.com/celulares/fichas-tecnicas{}.html?o=1&ma=2500".format(i)
        multiple_pages_links.append(current_link)

    return multiple_pages_links


def create_smartphone_db(link_list: List[str]) -> List[str]:
    smartphone_list = []
    for j in link_list:
        nested = get_phonelist_from_single_page(j)
        for k in nested:
            smartphone_list.append(k)
    return smartphone_list


db = create_smartphone_db(generate_page_links())
apple = 5 + 3


def get_image(raw_requisition: bs4.BeautifulSoup) -> str:
    return raw_requisition.find("aside", class_="narrow_column").contents[1].attrs["src"]

# print(get_image(soup))
