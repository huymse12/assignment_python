from bs4 import BeautifulSoup
import requests

import model
import repository
import db


def get_html_document(url):
    response = requests.get(url)
    return response.text


def format_money_to_float(value):
    return float(value.strip(" ").rstrip("₫").replace(",", ""))


def format_percent_int(value):
    return int(value.lstrip("-").rstrip("%"))


def get_name_and_brand(value):
    value = value.upper().lstrip("LAPTOP").strip(" ")
    value = value.lstrip("GAMING").strip(" ")
    arr = value.split(" ")
    brand = arr[0]
    name = " ".join(arr[1:])
    return name, brand


def get_laptop_data_from_url():
    mysql_db = db.connect_my_sql()
    laptop_repository = repository.LaptopBestSellerRepository(mysql_db)

    html_doc = get_html_document('https://gearvn.com/collections/laptop-gaming-ban-chay')
    soup = BeautifulSoup(html_doc, 'html.parser')
    print(soup.title.text)
    for div_element_product in soup.find_all("div", {"class": "product-row"}):
        product_name = div_element_product.find("h2", {"class": "product-row-name"})
        old_price = div_element_product.find("del")
        new_price = div_element_product.find("span", {"class": "product-row-sale"})
        best_seller_tag = div_element_product.find("span", {"class": "ico-product"})
        percent_discount = div_element_product.find("div", {"class": "new-product-percent"})
        name_and_brand = get_name_and_brand(product_name.text)
        print("name:{} - best_seller:{}".format(product_name.text, best_seller_tag is not None))
        laptop_entity = model.LaptopBestSellerEntity(name_and_brand[0],
                                                     format_money_to_float(old_price.text),
                                                     format_money_to_float(new_price.text),
                                                     format_percent_int(percent_discount.text),
                                                     best_seller_tag is not None)
        laptop_entity.set_brand(name_and_brand[1])
        print(laptop_entity.__dict__)
        laptop_repository.insert(laptop_entity)


get_laptop_data_from_url()
