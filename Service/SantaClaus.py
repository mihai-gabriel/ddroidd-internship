from __future__ import annotations

from Core.Letter import Letter


class SantaClaus:
    """
    A class to contain all methods to read/write to a file,
    build a report and generate a list of addresses grouped by city
    """
    __name: str
    _instance: SantaClaus

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

    def read_letter(self, filename) -> Letter:
        with open(filename, 'r') as f:
            next(f)  # ignore first line
            return Letter.parse_text(f.readlines())

    def write_letter(self, letter):
        with open(f"Letters/generated/letter-{letter.child.id}.txt", 'w') as f:
            f.write(f"Dear {self.__name},\n"
                    f"I am {letter.child.fullname}\n"
                    f"I am {letter.child.age} years old. I live at {letter.child.address}. "
                    f"I have been a very {letter.child.behavior_str} child this year\n"
                    f"What I would like the most this Christmas is:\n"
                    f"{letter.items_str}")
