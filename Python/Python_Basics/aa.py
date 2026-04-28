import tkinter as tk

questions = [
    {"question": "What is 2 + 2?", "answers": ["3", "4", "5", "6"], "correct": "4"},
    {"question": "Capital of France?", "answers": ["London", "Paris", "Rome", "Berlin"], "correct": "Paris"},
    {"question": "What color is the sky?", "answers": ["Green", "Red", "Blue", "Yellow"], "correct": "Blue"},
]

current = 0
score = 0
buttons = []

def check_answer(answer):
    global current, score
    
    if answer == questions[current]["correct"]:
        score += 1
        result_label.config(text="Correct! ✅", fg="green")
    else:
        result_label.config(text="Wrong! ❌", fg="red")
    
    score_label.config(text=f"Score: {score}")
    current += 1
    
    if current < len(questions):
        question_label.config(text=questions[current]["question"])
        for i, button in enumerate(buttons):
            button.config(text=questions[current]["answers"][i])
    else:
        question_label.config(text=f"Finished! Your score is {score}/{len(questions)}")
        for button in buttons:
            button.place_forget()

root = tk.Tk()
root.geometry("400x350")

question_label = tk.Label(root, text=questions[0]["question"])
question_label.place(x=50, y=30)

for i in range(4):
    btn = tk.Button(root, text=questions[0]["answers"][i],
                    command=lambda a=questions[0]["answers"][i]: check_answer(a))
    btn.place(x=50 + (i % 2) * 150, y=100 + (i // 2) * 50)
    buttons.append(btn)

result_label = tk.Label(root, text="")
result_label.place(x=50, y=220)

score_label = tk.Label(root, text="Score: 0")
score_label.place(x=50, y=260)

root.mainloop()