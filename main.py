from datetime import datetime

from Core.BehaviorEnum import BehaviorEnum
from Core.Child import Child
from Core.Item import Item
from Core.Letter import Letter
from Service.SantaClaus import SantaClaus


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
    print("Question 1. Constructing objects")

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
    """
    2. Reading letters using the Santa Claus service,
    populating letter instances (containing Child instances)
    and printing them to the console
    """
    print("\nQuestion 2. Reading letters")
    santa_service = SantaClaus()

    # Reading letter-0.txt through letter-2.txt
    for idx in range(0, 3):
        letter = santa_service.read_letter(f"Letters/manual/letter-{idx}.txt")
        print(letter)


def question3():
    """
    3. Generating letter files
    """
    print("\nQuestion 3")

    santa_service = SantaClaus()

    child1 = Child(0, "Tudor Tudorescu", 2012, "Str. Primaverii, Cluj-Napoca", BehaviorEnum.Good)
    letter1 = Letter(child1, datetime.now(), [Item(0, "Trenulet"), Item(1, "Robot")])

    child2 = Child(1, "Ion Vasile", 2009, "Str. Mihai Eminescu, Bucuresti", BehaviorEnum.Good)
    letter2 = Letter(child2, datetime.now(), [Item(1, "Robot"), Item(2, "Papusa")])

    child3 = Child(2, "Andrei Tanase", 2010, "Str. 6 Noiembrie, Suceava", BehaviorEnum.Bad)
    letter3 = Letter(child3, datetime.now(), [Item(3, "Acadea"), Item(1, "Robot")])

    for letter in [letter1, letter2, letter3]:
        santa_service.write_letter(letter)

    print("Letters generated!")


def question4():
    pass


def question5():
    pass


def question6():
    pass


if __name__ == '__main__':
    main()
