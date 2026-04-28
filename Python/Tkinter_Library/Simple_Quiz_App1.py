import tkinter as tk

questions = [
    {"question": "What is the capital of Sudan?", "answers": ["Khartoum", "Wad Madani", "Atbara", "Omdurman"], "correct": "Khartoum"},
    {"question": "When was the independence of Sudan?", "answers": ["1952", "1960", "1956", "1957"], "correct": "1956"},
    {"question": "In which part of Sudan is the Dinder national park?", "answers": ["Northeastern", "Southeastern", "East", "South"], "correct": "Southeastern"},
    {"question": "When was the Establishing of Gordon Memorial College (Khartoum Uni)?", "answers": ["1905", "1910", "1892", "1902"], "correct": "1902"},
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
        result_label.config(text=f"Wrong! ❌ Correct answer is: {questions[current]['correct']}", fg="red")

    score_label.config(text=f"Score: {score}")
    current += 1

    if current < len(questions):
        question_label.config(text=questions[current]["question"])
        for i, button in enumerate(buttons):
            button.config(text=questions[current]["answers"][i],
                          command=lambda a=questions[current]["answers"][i]: check_answer(a))
    else:
        question_label.config(text=f"Finished! Your score is {score}/{len(questions)} برضو عوير ")
        for button in buttons:
            button.place_forget()


root = tk.Tk()
root.title("Sudan George Kordahi")
root.geometry("600x400")
root.resizable(False, False)

question_label = tk.Label(root, text=questions[0]["question"], bg="#002AFF", fg="white", font=("Arial", 12, "bold"), wraplength=500)
question_label.place(x=50, y=30)

for i in range(4):
    btn = tk.Button(root, text=questions[0]["answers"][i], bg="#7289DA", fg="white",
                    font=("Arial", 11), border=0, width=20,
                    command=lambda a=questions[0]["answers"][i]: check_answer(a))
    btn.place(x=50 + (i % 2) * 250, y=100 + (i // 2) * 50)
    buttons.append(btn)

result_label = tk.Label(root, text="", bg="#FFFFFF", fg="white", font=("Arial", 11))
result_label.place(x=50, y=230)

score_label = tk.Label(root, text="Score: 0", bg="#002AFF", fg="white", font=("Arial", 11))
score_label.place(x=50, y=270)

root.mainloop()