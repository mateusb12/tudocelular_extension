from flask import Flask
from page_Scrapping import Requisicoes

app = Flask(__name__)


@app.route('/')
def get_all_phones():
    return Requisicoes().util.getSmartphones()


if __name__ == '__main__':
    app.run()
