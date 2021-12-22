from __future__ import annotations
from datetime import datetime
from typing import List

from Core import Item
from Core.Child import Child


class Letter:
    """
    Representation of a letter as an object.

    Contains information about the child who wrote the letter,
    the creation date and what items/toys the child wishes.
    """
    __child: Child
    __date: datetime
    __items: List[Item]

    def __init__(self, child: Child, date: datetime, items: List[Item]):
        """
        Filling private data members of letter instance
        :param child: Child instance
        :param date: Date and Time instance
        :param items: Toys/things children want, list of Item instances
        """
        self.__child = child
        self.__date = date
        self.__items = items

    def __str__(self) -> str:
        """
        The display of the letter
        :return: a string representation of the letter
        """
        return f"Child: {self.__child}\nDate: {self.__date}, Items: {[str(item) for item in self.__items]}"

    # @classmethod
    # def parse_text(cls, text: str) -> Letter:
    #
    #     pass