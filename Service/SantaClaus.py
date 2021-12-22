class SantaClaus:
    """
    A class to contain all methods to read/write to a file,
    build a report and generate a list of addresses grouped by city
    """
    name: str

    # _instance = None
    #
    # def __new__(cls, *args, **kwargs):
    #     if cls._instance is None:
    #         cls._instance = super(SantaClaus, cls).__new__(cls, *args, **kwargs)
    #     return cls._instance

    def __init__(self):
        self.name = "Santa Claus"
