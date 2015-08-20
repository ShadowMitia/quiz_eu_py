from random import randrange

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
        """Initialise variables and start quiz"""
        self.app_name = "Quiz EU"
        self.capital_question_template = "What is the capital of {}?"
        self.date_entry_question_template = "In what year did {} join the EU?"
        self.number_of_countries = 27
        self.score = 0
        self.countries = []
        self.capital = []
        self.date_entry = []
        self.members = european_members
        self.game()
        print("Your score: " + self.score + "/" + self.number_of_countries)

    def game(self, type="capital"):
        """Runs the quiz
           Args:
                type: which type of quiz is to be run
           Returns:
                nothing
        """
        question = None
        if type == "capital":
            question = self.capital_question_template
        elif type == "date_entry":
            question = self.date_entry_question_template
        looping = True
        while looping:  # Weeeee
            random_country = randrange(0, len(self.members), 1)
            print(question.format(european_members[random_country][0]))
            answer = input("-> ")
            if answer in ["q", "quit", "exit"]:
                looping = False
                return
            if type == "capital":
                if self.verify_answer(answer,
                                      self.members[random_country][1]):
                    self.score += 1
            elif type == "date_entry":
                if self.verify_answer(answer,
                                      self.members[random_country][2]):
                    self.score += 1
            if len(self.members) > 1:
                self.members.remove(self.members[random_country])
            else:
                looping = False

    def verify_answer(self, answer, real_answer):
        """Checks the input with the real answer
           Args:
                answer: input
                real_answer: the real answer
           Returns:
                True if the same, False otherwise
        """
        if answer.lower() == real_answer.lower():
            print("Correct!")
            return True
        else:
            print("Wrong answer: the answer was: " + real_answer)
            return False

if __name__ == "__main__":
    try:
        Quiz()
    except EOFError:
        print()
    except KeyboardInterrupt:
        print()
