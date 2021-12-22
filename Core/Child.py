from datetime import datetime

from Core.BehaviorEnum import BehaviorEnum


class Child:
    """
    A class used to represent a child who might get a present from Santa Claus.

    Contains information about his identity and behavior
    """
    __id: int
    __fullname: str
    __year_of_birth: int
    __address: str
    __behavior: BehaviorEnum

    def __init__(self, id_: int, fullname: str, date_of_birth: int, address: str, behavior: BehaviorEnum):
        self.__id = id_
        self.__fullname = fullname
        self.__year_of_birth = date_of_birth
        self.__address = address
        self.__behavior = behavior

    def __str__(self):
        return f"ID: {self.__id}, Name: {self.__fullname}, Year of birth: {self.__year_of_birth}, " \
               f"Address: {self.__address}, Behavior: {self.__behavior}"

    @property
    def age(self) -> int:
        """ Computes age based on year of birth """
        return datetime.now().year - self.__year_of_birth
