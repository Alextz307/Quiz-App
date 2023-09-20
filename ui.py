from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
SECOND_TO_MS = 1000


class QuizUI:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label()
        self.score_label.config(text='Score: 0', bg=THEME_COLOR, fg='white')
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas()
        self.canvas.config(width=300, height=250, bg='white', highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 125,
            text='Some question text',
            fill=THEME_COLOR,
            font=('Arial', 20, 'italic'),
            width=280
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.wrong_button = Button(command=self.wrong_answer)
        wrong_image = PhotoImage(file='images/false.png')
        self.wrong_button.config(image=wrong_image,
                                 borderwidth=0, border=0, bd=0, padx=0, pady=0, highlightthickness=0)
        self.wrong_button.grid(row=2, column=0)

        self.correct_button = Button(command=self.correct_answer)
        correct_image = PhotoImage(file='images/true.png')
        self.correct_button.config(image=correct_image,
                                   borderwidth=0, border=0, bd=0, padx=0, pady=0, highlightthickness=0)
        self.correct_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')

        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.correct_button.config(state='disabled')
            self.wrong_button.config(state='disabled')

    def correct_answer(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def wrong_answer(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
            self.score_label.config(text=f'Score: {self.quiz.score}')
        else:
            self.canvas.config(bg='red')

        self.window.after(SECOND_TO_MS, self.get_next_question)
