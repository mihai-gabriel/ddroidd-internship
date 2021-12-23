from __future__ import annotations

import os
from collections import Counter
from typing import List

from Core.Letter import Letter


class SantaClaus:
    """
    A class to contain all methods to read/write to a file,
    build a report and generate a list of addresses grouped by city
    """
    __name: str
    _instance: SantaClaus
    _base_path: str

    _instance = None
    _base_path = "./Letters/generated"

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

    def read_letter(self, filename) -> Letter:
        """ Method to read from a file and return a Letter instance """
        with open(filename, 'r') as f:
            next(f)  # ignore first line
            return Letter.parse_text(f.readlines())

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
            with open(os.path.join(self._base_path, filename), 'r') as f:
                line: str = f.readlines()[-1]  # the last line in the file
                for item in line.split(','):
                    items.append(item)

        report = Counter(items)

        return dict(report.most_common())  # returning in descending order by quantity
