class Quiz_Brain:
    def __init__(self, number, list):
        self.number = 0
        self.list = list

    def next_question(self):
        question = self.list[self.number]
        input (f"Q.{self.number}: {question}. (True / False)? \n")