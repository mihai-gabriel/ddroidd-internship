class Item:
    """ Toys/items that should be distributed to good behaving kids """
    __id: int
    __name: str

    def __init__(self, id_, name):
        self.__id = id_
        self.__name = name

    def __str__(self):
        return f"ID: {self.__id}, Name: {self.__name}"
