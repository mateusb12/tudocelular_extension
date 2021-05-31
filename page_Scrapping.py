from typing import List

from bs4 import BeautifulSoup
import requests

from util import Util


class Requisicoes:
    def __init__(self):
        self.multiple_pages_links = dict()
        self.db = self.create_smartphone_db(self.generate_page_links())

        self.util = Util(self.db)
        print(self.util.getSmartphones())

    def get_phonelist_from_single_page(self, page_id: str) -> List[str]:
        # Tentar otimizar as chamadas, ainda demora mt
        html = requests.get(page_id).content
        soup = BeautifulSoup(html, 'html.parser')
        list_body = soup.find_all("a", class_="vedi_prezzi")
        smartphone_ids = list(map(
            lambda x: "https://www.tudocelular.com" + x.attrs['href'].replace('precos', 'fichas-tecnicas'), list_body))

        return smartphone_ids

    def generate_page_links(self) -> dict:
        available_pages = ["", "_2", "_3", "_4", "_5"]

        for i in available_pages:
            if i not in self.multiple_pages_links:
                current_link = f"https://www.tudocelular.com/celulares/fichas-tecnicas{i}.html?o=1&ma=2500"
                self.multiple_pages_links[i] = current_link

        return self.multiple_pages_links

    def create_smartphone_db(self, link_list: dict) -> List[str]:
        smartphone_list = []

        for j in link_list.values():
            smartphone_list.extend(self.get_phonelist_from_single_page(j))

        return smartphone_list
