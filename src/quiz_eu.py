
european_members = [
    ("Austria", "Vienna", 1995),
    ("Belgium", "Brussels", 1952),
    ("Bulgaria", "Sofia", 2007),
    ("Croatia", "Zagreb", 2013),
    ("Cyprus", "Nicosia", 2004),
    ("Czech Republic", "Prague", 2004),
    ("Denmark", "Copenhagen", 1973),
    ("Estonia", "Tallinn", 2004),
    ("Finland", "Helsinki", 1995),
    ("France", "Paris", 1952),
    ("Germany", "Berlin", 1952),
    ("Greece", "Athens", 1981),
    ("Hungary", "Budapest", 2004),
    ("Ireland", "Dublin", 1973),
    ("Italy", "Rome", 1952),
    ("Latvia", "Riga", 2004),
    ("Lithuania", "Vilnius", 2004),
    ("Luxembourg", "Luxembourg", 1952),
    ("Malta", "Valletta", 2004),
    ("Netherlands", "Amsterdam", 1952),
    ("Poland", "Warsaw", 2004),
    ("Portugal", "Lisbon", 1986),
    ("Romania", "Bucharest", 2007),
    ("Slovakia", "Bratislava", 2004),
    ("Slovenia", "Ljubljana", 2004),
    ("Spain", "Madrid", 1986),
    ("Sweden", "Stockholm", 1995),
    ("United Kindgom", "London", 1973),
]


class Quiz():

    def __init__(self):
        self.app_name = "Quiz EU"
        self.capital_question_template = "What is the capital of {}?"
        self.date_entry_question_template = "In what year did {} join the EU?"
        self.countries = []
        self.capital = []
        self.date_entry = []


if __name__ == "__main__":
    Quiz()
