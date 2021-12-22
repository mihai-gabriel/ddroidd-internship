from datetime import datetime

from Core.BehaviorEnum import BehaviorEnum
from Core.Child import Child
from Core.Item import Item
from Core.Letter import Letter


def main():
    question1()
    question2()
    question3()
    question4()
    question5()
    question6()


def question1():
    """
    I made use of each class related to child and letter.
    `Letter.__str__()` contains `Child.__str__()` so I only need to print the letter
    """
    print("Question 1")

    child1 = Child(0, "Tudor Tudorescu", 2012, "Str. Primaverii, Cluj-Napoca", BehaviorEnum.Good)
    letter1 = Letter(child1, datetime.now(), [Item(0, "Trenulet"), Item(1, "Robot")])

    print(f"{letter1}")

    child2 = Child(1, "Ion Vasile", 2009, "Str. Mihai Eminescu, Bucuresti", BehaviorEnum.Good)
    letter2 = Letter(child2, datetime.now(), [Item(1, "Robot"), Item(2, "Papusa")])

    print(f"{letter2}")

    child3 = Child(2, "Andrei Tanase", 2010, "Str. 6 Noiembrie, Suceava", BehaviorEnum.Bad)
    letter3 = Letter(child3, datetime.now(), [Item(3, "Acadea"), Item(1, "Robot")])

    print(f"{letter3}")


def question2():
    pass


def question3():
    pass


def question4():
    pass


def question5():
    pass


def question6():
    pass


if __name__ == '__main__':
    main()
