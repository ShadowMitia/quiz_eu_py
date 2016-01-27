#!/bin/python

from random import randrange


class Quiz():

    def __init__(self, members):
        """Initialise variables and start quiz"""
        self.app_name = "Quiz EU"
        self.capital_question_template = "What is the capital of {}?"
        self.date_entry_question_template = "In what year did {} join the EU?"
        self.number_of_countries = 27
        self.score = 0
        self.countries = []
        self.capital = []
        self.date_entry = []
        self.members = members
        self.game()
        print("Your score: " + str(self.score) + "/"
              + str(self.number_of_countries))

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
            print(question.format(self.members[random_country][0]))
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
