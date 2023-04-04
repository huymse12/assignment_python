class LaptopBestSellerEntity:
    def __init__(self, name, old_price, new_price, percent_discount, best_seller):
        self.name = name
        self.old_price = old_price
        self.new_price = new_price
        self.percent_discount = percent_discount
        self.best_seller = best_seller
        self.brand = ""
        self.id = 0

    def set_brand(self, brand):
        self.brand = brand

    def set_id(self, id_laptop):
        self.id = id_laptop


class ResponseAPI(object):
    def __init__(self, code, message, data):
        self.code = code
        self.message = message
        self.data = data


def success_response(data):
    return ResponseAPI(200, "Success", data)


def bad_request_response(message):
    return ResponseAPI(404, message, None)


def internal_error_response(message):
    return ResponseAPI(500, message, None)
