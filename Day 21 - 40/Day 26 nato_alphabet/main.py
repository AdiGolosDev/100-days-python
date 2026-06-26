# list comprehension
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers] # [new_item for item in list]
print(new_list)

name = "Klokan"
letters_list = [letter for letter in name]
print(letters_list)

new_num_list = [number * 2 for number in range(1, 5)]
print(new_num_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_cap_names = [name.upper() for name in names if len(name) > 4]
print(long_cap_names)

# dictionary comprehensions
import random
student_scores = {student:random.randint(1, 100) for student in names}
print(student_scores)

passing_students = {student:student_scores[student] for student in student_scores if student_scores[student] > 50} # first try
passing_students = {student:score for (student, score) in student_scores.items() if score >= 60} # second try
print(passing_students)

# pandas DataFrame comprehension
import pandas
student_dict = {
    "student": ["James", "Angela", "Klokan"],
    "score": [50, 70, 22]
}
student_df = pandas.DataFrame(student_dict)
print(student_df)

for (index, row) in student_df.iterrows():
    print(row.student)
    print(row.score)
    if row.student == "Klokan":
        print("this guy is cool")
