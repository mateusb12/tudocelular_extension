from typing import List

import bs4
from bs4 import BeautifulSoup
import requests
from smartphone_scrapping import Util


class Requisicoes:
    def __init__(self):
        self.multiple_pages_links = dict()
        self.db = self.create_smartphone_db(self.generate_page_links())

        self.util = Util(self.db)

    def get_phonelist_from_single_page(self, page_id: str) -> List[str]:
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

    def generate_page_links(self) -> dict:
        sequence = ["", "_2", "_3", "_4", "_5"]

        # for i in sequence:
        for i in range(3):
            if i not in self.multiple_pages_links.keys():
                current_link = f"https://www.tudocelular.com/celulares/fichas-tecnicas{sequence[i]}.html?o=1&ma=2500"
                self.multiple_pages_links[i] = current_link

        return self.multiple_pages_links

    def create_smartphone_db(self, link_list: dict) -> List[str]:
        smartphone_list = []

        for j in link_list.values():
            nested = self.get_phonelist_from_single_page(j)
            for k in nested:
                smartphone_list.append(k)

        return smartphone_list
