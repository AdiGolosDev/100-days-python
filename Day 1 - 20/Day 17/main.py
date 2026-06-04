from data import question_data
import question_model
import quiz_brain
import random

question_bank = []

for item in question_data:
    q = question_model.Question(item["text"], item["answer"])
    question_bank.append(q)

random.shuffle(question_bank)

brain_one = quiz_brain.Quiz_Brain(0, 0, question_bank)
while brain_one.still_has_questions():
    brain_one.next_question()

print(f"You've completed the quiz.\nYour final score was: {brain_one.score}/{brain_one.number}")
