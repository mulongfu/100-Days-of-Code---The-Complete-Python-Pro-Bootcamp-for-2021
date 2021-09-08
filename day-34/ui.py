import tkinter
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label=tkinter.Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.q_text = self.canvas.create_text(150, 125, width=280, text="Some Question Text", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        true_img = tkinter.PhotoImage(file="images/true.png")
        self.true_btn = tkinter.Button(image=true_img, highlightthickness=1, command=self.true_pressed)
        self.true_btn.grid(row=2, column=0)

        false_img = tkinter.PhotoImage(file="images/false.png")
        self.false_btn = tkinter.Button(image=false_img, highlightthickness=1, command=self.false_pressed)
        self.false_btn.grid(row=2, column=1)
        self.get_next_q()
        self.window.mainloop()

    def get_next_q(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():            
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=q_text)
        else:
            self.canvas.itemconfig(self.q_text, text="reached the end of question.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_q)