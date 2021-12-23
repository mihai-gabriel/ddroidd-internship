class Item:
    """ Toys/items that should be distributed to good behaving kids """
    __id: int
    __name: str

    def __init__(self, id_, name):
        self.__id = id_
        self.__name = name

    def __str__(self) -> str:
        return f"ID: {self.__id}, Name: {self.__name}"

    @property
    def name(self) -> str:
        return self.__name

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, new_id: int):
        self.__id = new_id
