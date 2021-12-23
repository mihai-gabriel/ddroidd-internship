from __future__ import annotations

import re
from datetime import datetime
from typing import List

from Core.Item import Item
from Core.BehaviorEnum import BehaviorEnum
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
        return f"Child: {self.__child}\nDate: {self.date}, Items: {[str(item) for item in self.__items]}\n"

    @classmethod
    def parse_text(cls, text: List[str]) -> Letter:
        """
        Filling data from a letter file
        :param text: List of each line in a letter read from a file
        :return: Letter instance with parsed data
        """
        # Matching `I am [FULL_NAME]`
        name_pattern = re.compile(r"(I am )([A-Za-z ]+)")

        # Taking the second group which include characters and spaces from the first line
        fullname = name_pattern.match(text[0]).group(2)

        # Matching `I am [AGE] years old. I live at [ADDRESS]. I have been a very [BEHAVIOR] child this year`
        info_pattern = re.compile(r"(I am )([0-9]+)( years old. I live at )([A-Za-z0-9-., ]+)"
                                  r"(. I have been a very )([A-Za-z]+)( child this year)")

        # Interested only in second, fourth and sixth groups
        info_result = info_pattern.match(text[1])
        age, address, behavior = info_result.group(2), info_result.group(4), info_result.group(6)

        # converting string to enum
        behavior_enum = BehaviorEnum.Good if behavior == "good" else BehaviorEnum.Bad

        items = [Item(0, item_name) for item_name in text[3].split(',')]
        child = Child(0, fullname, datetime.now().year - int(age), address, behavior_enum)

        return cls(child, datetime.now(), items)

    @property
    def child(self) -> Child:
        return self.__child

    @property
    def date(self):
        return self.__date.strftime("%Y-%m-%d")

    @property
    def items(self) -> List[Item]:
        return self.__items

    @property
    def items_str(self) -> str:
        return ",".join([item.name for item in self.__items])
