import question_model
import data
import quiz_brain

question_bank = [question_model.Question(i['question'], i['correct_answer']) for i in data.question_data]

quiz_brain_o = quiz_brain.QuizBrain(question_bank)

while quiz_brain_o.still_has_question():
    quiz_brain_o.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz_brain_o.score}/{len(question_bank)}")