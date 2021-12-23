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

    def __init__(self, id_: int, fullname: str, year_of_birth: int, address: str, behavior: BehaviorEnum):
        self.__id = id_
        self.__fullname = fullname
        self.__year_of_birth = year_of_birth
        self.__address = address
        self.__behavior = behavior

    def __str__(self):
        return f"ID: {self.__id}, Name: {self.__fullname}, Year of birth: {self.__year_of_birth}, " \
               f"Address: {self.__address}, Behavior: {self.behavior_str}"

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, new_id: int):
        self.__id = new_id

    @property
    def fullname(self) -> str:
        return self.__fullname

    @property
    def address(self) -> str:
        return self.__address

    @property
    def city(self):
        """
        Parsing city name from address format '<Street Name> <Number>, <City Name>'
        Any other type of format would potentially require the use of regular expression,
        since I won't use here due to the simplicity of the format.
        """
        return self.__address.split(',')[-1].strip()

    @property
    def behavior(self) -> BehaviorEnum:
        return self.__behavior

    @property
    def behavior_str(self) -> str:
        """ Convenient way of storing the enum """
        return "good" if self.__behavior is BehaviorEnum.Good else "bad"

    @property
    def year_of_birth(self) -> int:
        return self.__year_of_birth

    @property
    def age(self) -> int:
        """ Computes age based on year of birth """
        return datetime.now().year - self.__year_of_birth
