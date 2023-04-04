from abc import ABC, abstractmethod
import repository
import model


def _get_data(field, value):
    if field in value:
        return value[field]
    return None


class ILaptopBestSellerService(ABC):
    @abstractmethod
    def create_laptop(self, request):
        pass

    @abstractmethod
    def edit_laptop(self, request, id_laptop):
        pass

    @abstractmethod
    def list_laptop(self):
        pass

    @abstractmethod
    def get_detail_laptop(self, id_laptop):
        pass

    @abstractmethod
    def delete_laptop(self, id_laptop):
        pass


class LaptopBestSellerService(ILaptopBestSellerService):

    def __init__(self, laptop_repository: repository.ILaptopBestSellerRepository):
        self._laptop_repository = laptop_repository

    def create_laptop(self, request):
        try:
            entity = model.LaptopBestSellerEntity(request["name"], request["old_price"],
                                                  request["new_price"], request["percent_discount"],
                                                  request["best_seller"])
            entity.set_brand(request["brand"])
            self._laptop_repository.insert(entity)
            return model.success_response("Success").__dict__
        except Exception as e:
            print(e)
            return model.internal_error_response("Internal Error").__dict__

    def edit_laptop(self, request, id_laptop):
        try:
            laptop = self._laptop_repository.get_detail_laptop(id_laptop)
            if laptop is None:
                return model.bad_request_response("Laptop not found").__dict__
            entity = model.LaptopBestSellerEntity(
                _get_data("name", request),
                _get_data("old_price", request),
                _get_data("new_price", request),
                _get_data("percent_discount", request),
                _get_data("best_seller", request)
            )
            entity.set_brand(_get_data("brand", request))
            self._laptop_repository.edit(entity, id_laptop)
            return model.success_response("Success").__dict__

        except Exception as e:
            print(e)
            return model.internal_error_response("Internal Error").__dict__

    def list_laptop(self):
        try:
            data = self._laptop_repository.get_laptop()
            arr_laptop = []
            for laptop_element in data:
                entity = model.LaptopBestSellerEntity(
                    laptop_element[0], laptop_element[1], laptop_element[2], laptop_element[3],
                    laptop_element[4])
                entity.set_brand(laptop_element[6])
                entity.set_id(laptop_element[5])
                arr_laptop.append(entity.__dict__)
            return model.success_response(arr_laptop).__dict__
        except Exception as e:
            print(e)
            return model.internal_error_response("Internal Error").__dict__

    def get_detail_laptop(self, id_laptop):
        pass

    def delete_laptop(self, id_laptop):
        try:
            laptop = self._laptop_repository.get_detail_laptop(id_laptop)
            if laptop is None:
                return model.bad_request_response("laptop not found").__dict__
            self._laptop_repository.delete_laptop(id_laptop)
            return model.success_response("Delete success").__dict__
        except Exception as e:
            print(e)
            return model.internal_error_response("Internal Error").__dict__
