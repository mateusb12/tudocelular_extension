import requests
from bs4 import BeautifulSoup


class Util:
    def __init__(self, smartphone_links):
        self.smartphone_links = smartphone_links
        self.smartphones = dict()

        for link in smartphone_links:

            if link not in self.smartphones.keys():
                html = requests.get(link).content
                soup = BeautifulSoup(html, 'html.parser')
                self.smartphones[link] = Smartphone(
                    *self.get_name_and_image(soup),
                    *self.get_price_and_store(soup),
                    *self.get_grades(soup)
                )

    def get_name_and_image(self, soup) -> [str, str]:
        raw_image = soup.find("aside", class_="narrow_column").contents[1]
        if raw_image:
            name, img = raw_image.attrs["alt"], raw_image.attrs["src"]
            return name, img

        return '', ''

    def get_price_and_store(self, soup) -> [str, str]:
        raw_price = soup.find("a", class_="hoverred")
        if raw_price:
            price, store = raw_price.text, raw_price.attrs["href"]
            return price, store

        return ['', '']

    def get_grades(self, soup) -> [str, str, str]:
        raw_columns = soup.find("div", class_="phone_column").find_all("ul", class_="phone_column_features")

        camera_grade = performance_grade = battery_grade = None

        for column in raw_columns:
            if '/ 10' in column.text:
                grades = list(filter(lambda x: not x.isalpha(), column.text.split("/ 10")))
                camera_grade, performance_grade = grades[3], grades[4]
                continue

            if 'mAh' in column.text:
                # Calcular, por agora, a nota da bateria como math.min(0, <bateria do celular>/500-, 10)
                battery_grade = int(''.join(list(filter(lambda x: not x.isalpha(), column.text.split(" ")[0]))))
                battery_grade = min(round(battery_grade, 2)/500, 10)
                break

        return [camera_grade, performance_grade, battery_grade]

    def getSmartphones(self):
        result = ', '.join(list(map(str, self.smartphones.values())))
        return result


class Smartphone:
    def __init__(self, name, image, price, store, camera_grade, performance_grade, battery_grade):
        self.name = name
        self.image = image
        self.price = price
        self.store = store
        self.camera_grade = camera_grade
        self.performance_grade = performance_grade
        self.battery_grade = battery_grade

    def __str__(self):
        return 'name: {0}, image: {1}, price: {2}, store: {3}, camera_grade: {4}, performance_grade: {5}, ' \
               'battery_grade: {6}'.format(
            self.name,
            self.image,
            self.price,
            self.store,
            self.camera_grade,
            self.performance_grade,
            self.battery_grade
        )
