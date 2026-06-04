class Quiz_Brain:
    def __init__(self, number, score, list):
        self.number = 0
        self.score = 0
        self.list = list

    def next_question(self):
        question = self.list[self.number]
        user_answer = input(f"Q.{self.number + 1}: {question.text} (True / False)? \n").lower()
        if user_answer != "true" and user_answer != "false":
            print("Please enter 'True' or 'False'.")
            self.next_question()
        else:
            self.check_answer(user_answer)
    
    def check_answer(self, user_answer):
        correct_answer = self.list[self.number].answer.lower()
        if user_answer == correct_answer:
            self.score += 1
            print(f"You got it right!\nThe correct answer was: {correct_answer}")
            self.number += 1
            print(f"Your current score is: {self.score}/{self.number}\n")
        else:
            print(f"That's wrong.\nThe correct answer was: {correct_answer}")
            self.number += 1
            print(f"Your current score is: {self.score}/{self.number}\n")

    def still_has_questions(self):
        if self.number < len(self.list)-1:
            return True
        else:
            return False
