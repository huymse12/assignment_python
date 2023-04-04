from abc import ABC, abstractmethod


class ILaptopBestSellerRepository(ABC):
    @abstractmethod
    def insert(self, entity):
        pass

    @abstractmethod
    def edit(self, entity, id_laptop):
        pass

    @abstractmethod
    def get_detail_laptop(self, id_laptop):
        pass

    @abstractmethod
    def delete_laptop(self, id_laptop):
        pass

    @abstractmethod
    def get_laptop(self):
        pass


class LaptopBestSellerRepository(ILaptopBestSellerRepository):

    def get_laptop(self):
        sql = 'select * from LAPTOPBESTSELLER'
        cursor = self.mysql_db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

    def delete_laptop(self, id_laptop):
        sql = 'delete from LAPTOPBESTSELLER where ID = {}'.format(id_laptop)
        cursor = self.mysql_db.cursor()
        cursor.execute(sql)
        self.mysql_db.commit()

    def get_detail_laptop(self, id_laptop):
        sql = 'select * from LAPTOPBESTSELLER where ID = {}'.format(id_laptop)
        cursor = self.mysql_db.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()
        return data

    def edit(self, entity, id_laptop):
        update_arr = []
        value = []
        if entity.name is not None:
            update_arr.append("Name=%s")
            value.append(entity.name)

        if entity.old_price is not None:
            update_arr.append("OldPrice=%s")
            value.append(entity.old_price)

        if entity.new_price is not None:
            update_arr.append("NewPrice=%s")
            value.append(entity.new_price)

        if entity.percent_discount is not None:
            update_arr.append("PercentDiscount=%s")
            value.append(entity.percent_discount)

        if entity.best_seller is not None:
            update_arr.append("BestSeller=%s")
            value.append(entity.best_seller)

        if entity.brand is not None:
            update_arr.append("Brand=%s")
            value.append(entity.brand)

        if len(update_arr) > 0:
            sql = "update LAPTOPBESTSELLER set {} where  ID = {}".format(",".join(update_arr), id_laptop)
            cursor = self.mysql_db.cursor()
            cursor.execute(sql, value)
            self.mysql_db.commit()

    def __init__(self, mysql_db):
        self.mysql_db = mysql_db

    def insert(self, entity):
        sql = "insert into LAPTOPBESTSELLER(Name, OldPrice, NewPrice, PercentDiscount, BestSeller, Brand) " \
              "VALUES (%s,%s,%s,%s,%s,%s)"
        value = (entity.name, entity.old_price, entity.new_price, entity.percent_discount,
                 entity.best_seller, entity.brand)
        cursor = self.mysql_db.cursor()
        cursor.execute(sql, value)
        self.mysql_db.commit()
