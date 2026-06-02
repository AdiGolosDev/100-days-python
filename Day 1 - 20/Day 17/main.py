from data.py import question_data
import question_model.py

question_bank = []

for item in question_data:
    q = question_model.Question(item["text"], item["answer"])
    question_bank.append(q)