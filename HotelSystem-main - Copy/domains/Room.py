class Room():
    def __init__(self, id, type, price):
        self.__id = id
        self.__type = type
        self.__price = price

    
    def get_id(self):
        return self.__id
    def get_type(self):
        return self.__type
    def get_price(self):
        return self.__price


    def set_id(self, id):
        self.__id = id
    def set_type(self, type):
        self.__type = type
    def set_price(self, price):
        self.__price = price

    