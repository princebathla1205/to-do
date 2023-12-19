import json

with open("question.json",'r') as file:
    content = file.read()

data = json.loads(content)
score = 0
for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, alternative)
    user_answer = int(input("Enter your answer: "))
    question["user_choice"] = user_answer


for index, answer in enumerate(data):
    if answer["correct_answer"] == answer["user_choice"]:
        score = score + 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"
    message = f"{index + 1 } {result} - Your answer {answer['user_choice']}, Correct Answer {answer['correct_answer']}"
    print(message)

print("Score", score, "/", len(data))

