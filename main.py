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

    child1 = Child(0, "Tudor Tudorescu", 2012, "Str. Primaverii Nr. 21, Cluj-Napoca", BehaviorEnum.Good)
    letter1 = Letter(child1, datetime.now(), [Item(0, "Trenulet"), Item(1, "Robot")])
    print(letter1)

    child2 = Child(1, "Ion Vasile", 2009, "Str. Mihai Eminescu Nr. 15, Bucuresti", BehaviorEnum.Good)
    letter2 = Letter(child2, datetime.now(), [Item(1, "Robot"), Item(2, "Papusa")])
    print(letter2)

    child3 = Child(2, "Andrei Tanase", 2010, "Str. 6 Noiembrie Nr. 10, Cluj-Napoca", BehaviorEnum.Bad)
    letter3 = Letter(child3, datetime.now(), [Item(3, "Acadea"), Item(1, "Robot")])
    print(letter3)


def question2():
    """
    Reading letters using the Santa Claus service,
    populating letter instances (containing Child instances)
    and printing them to the console
    """
    print("\nQuestion 2. Reading letters")
    santa_service = SantaClaus()  # constructor uses the Singleton Pattern

    # Reading letter-0.txt through letter-2.txt
    for idx in range(0, 3):
        letter: Letter = santa_service.read_letter(f"Letters/manual/letter-{idx}.txt")
        print(letter)


def question3():
    """
    Generating letter files from objects
    """
    print("\nQuestion 3. Generate files")

    santa_service = SantaClaus()

    child1 = Child(0, "Tudor Tudorescu", 2012, "Str. Primaverii Nr. 21, Cluj-Napoca", BehaviorEnum.Good)
    letter1 = Letter(child1, datetime.now(), [Item(0, "Trenulet"), Item(1, "Robot")])

    child2 = Child(1, "Ion Vasile", 2009, "Str. Mihai Eminescu Nr. 15, Bucuresti", BehaviorEnum.Good)
    letter2 = Letter(child2, datetime.now(), [Item(1, "Robot"), Item(2, "Papusa")])

    child3 = Child(2, "Andrei Tanase", 2010, "Str. 6 Noiembrie Nr. 10, Cluj-Napoca", BehaviorEnum.Bad)
    letter3 = Letter(child3, datetime.now(), [Item(3, "Acadea"), Item(1, "Robot")])

    for letter in [letter1, letter2, letter3]:
        santa_service.write_letter(letter)

    print("Letters generated!")


def question4():
    """
    Report of the quantity of each toy the elves need to build
    """
    print("\nQuestion 4. Building report")
    santa_service = SantaClaus()
    report: dict = santa_service.build_report()

    for toy_name, quantity in report.items():
        print(f"{toy_name} - {quantity}")


def question5():
    """
    Given the fact that I used `SantaClaus()` as a service,
    I only need to instantiate it once and use multiple times across all question solutions,
    so redundant re-creation does not take place, acting as a lazy loading.

    As a consequence, the Singleton Pattern is favorable
    and I already implemented it. I will leave a quick test
    """
    print("\nQuestion 5. Singleton Pattern")

    santa_service1 = SantaClaus()
    santa_service2 = SantaClaus()

    assert (santa_service1 is santa_service2)  # Note `is` operator checks if the object is the same in memory
    print(f"Is SantaClaus service a Singleton class? {santa_service1 is santa_service2}")


def question6():
    """
    Travel Itinerary.
    Grouping all addresses by city.
    Since the address format that I used is something like '<Street Name> <Number>, <City Name>',
    I will parse the <City Name> according to this format.
    """
    print("\nQuestion 6. Grouping addresses by city")

    santa_service = SantaClaus()
    all_addresses: dict = santa_service.travel_itinerary()

    for city, addresses in all_addresses.items():
        print(f"{city}: {addresses}")


if __name__ == '__main__':
    main()
