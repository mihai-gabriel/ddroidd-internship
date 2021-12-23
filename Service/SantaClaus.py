from __future__ import annotations

import os
import platform
from collections import Counter, defaultdict
from datetime import datetime
from typing import List

from Core.BehaviorEnum import BehaviorEnum
from Core.Letter import Letter


class SantaClaus:
    """
    A class to contain all methods to read/write to a file,
    build a report and generate a list of addresses grouped by city
    """
    # type annotations
    __name: str
    _instance: SantaClaus
    _base_path: str
    _items: List[str]
    _no_children: int

    # class fields
    _instance = None

    def __new__(cls):
        """
        Using the Singleton Pattern to have a single instance across all question solution functions/methods
        If `self._instance` is None, we create an instance, otherwise we retrieve it and not re-create it.
        """
        if cls._instance is None:
            cls._instance = super(SantaClaus, cls).__new__(cls)

        return cls._instance

    def __init__(self):
        self.__name = "Santa Claus"
        self._base_path = "./Letters/generated"
        self._items = []
        self._no_children = 0

    def read_letter(self, filename) -> Letter:
        """ Method to read from a file and return a Letter instance """
        with open(filename, 'r') as f:
            next(f)  # ignore first line
            letter = Letter.parse_text(f.readlines())

            # Only on Windows, getting creation date
            if platform.system() == "Windows":
                letter.date = datetime.fromtimestamp(os.path.getctime(filename))

            # setting items id
            for item in letter.items:
                if item.name in self._items:
                    item.id = self._items.index(item.name)
                else:
                    item.id = len(self._items)
                    self._items.append(item.name)

            # setting child id
            letter.child.id = self._no_children
            self._no_children += 1

            return letter

    def write_letter(self, letter: Letter):
        """ Writing a letter file from an instance of a Letter using given template """
        with open(os.path.join(self._base_path, f"letter-{letter.child.id}.txt"), 'w') as f:
            f.write(f"Dear {self.__name},\n"
                    f"I am {letter.child.fullname}\n"
                    f"I am {letter.child.age} years old. I live at {letter.child.address}. "
                    f"I have been a very {letter.child.behavior_str} child this year\n"
                    f"What I would like the most this Christmas is:\n"
                    f"{letter.items_str}")

    def build_report(self) -> dict:
        """
        Using a dictionary (hashmap) to store the name of the toy as a key and
        the quantity as a value

        :return: dictionary sorted in descending order containing the report
        """
        items: List[str] = []

        for filename in os.listdir(path=self._base_path):
            letter: Letter = self.read_letter(os.path.join(self._base_path, filename))
            if letter.child.behavior is BehaviorEnum.Good:
                items.extend([item.name for item in letter.items])

        report = Counter(items)
        return dict(report.most_common())  # returning in descending order by quantity

    def travel_itinerary(self) -> dict:
        """
        Grouping addresses by city using a dictionary,
        each key will be a city and each value will be a list of addresses

        :return: all addresses grouped by city for good behaving children
        """
        itinerary: dict = defaultdict(list)

        # fetching all addresses from the letters
        for filename in os.listdir(path=self._base_path):
            letter: Letter = self.read_letter(os.path.join(self._base_path, filename))
            if letter.child.behavior is BehaviorEnum.Good:
                itinerary[letter.child.city].append(letter.child.address)

        return itinerary
