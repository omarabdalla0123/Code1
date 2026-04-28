import os
import shutil
import tkinter as tk
from tkinter import messagebox

DOWNLOADS = os.path.join(os.path.expanduser("~"), "Downloads")

RULES = [
    {"tag": "(PT)", "folder": "product tamples", "color": "#2563EB", "light": "#EFF6FF"},
    {"tag": "(CF)", "folder": "CF_Files",         "color": "#059669", "light": "#ECFDF5"},
]

def scan():
    for rule in RULES:
        rule["listbox"].delete(0, tk.END)
        rule["count"].config(text="")

    total = 0
    for filename in os.listdir(DOWNLOADS):
        name, ext = os.path.splitext(filename)
        name_stripped = name.strip()
        for rule in RULES:
            if name_stripped.endswith(rule["tag"]):
                rule["listbox"].insert(tk.END, "  " + filename)
                total += 1

    for rule in RULES:
        n = rule["listbox"].size()
        rule["count"].config(text=f"{n} file{'s' if n != 1 else ''}")

    move_btn.config(state=tk.NORMAL if total > 0 else tk.DISABLED)
    status_var.set(f"Found {total} file(s) ready to sort." if total else "No matching files found in Downloads.")

def move_all():
    moved = 0
    errors = []

    for rule in RULES:
        files = rule["listbox"].get(0, tk.END)
        if not files:
            continue
        dest = os.path.join(DOWNLOADS, rule["folder"])
        os.makedirs(dest, exist_ok=True)
        for entry in files:
            filename = entry.strip()
            src = os.path.join(DOWNLOADS, filename)
            dst = os.path.join(dest, filename)
            try:
                shutil.move(src, dst)
                moved += 1
            except Exception as e:
                errors.append(f"{filename}: {e}")

    scan()

    if errors:
        messagebox.showerror("Errors", "\n".join(errors))
    else:
        status_var.set(f"Done! Moved {moved} file(s) successfully.")

# ── Window ──────────────────────────────────────────────────────────────
root = tk.Tk()
root.title("File Sorter")
root.geometry("540x540")
root.resizable(False, False)
root.configure(bg="#F8F9FA")

status_var = tk.StringVar(value="Click Scan to detect files in your Downloads folder.")

# ── Header ───────────────────────────────────────────────────────────────
header = tk.Frame(root, bg="#1E293B", padx=20, pady=16)
header.pack(fill=tk.X)

tk.Label(header, text="File Sorter", font=("Segoe UI", 15, "bold"),
         bg="#1E293B", fg="white").pack(anchor="w")
tk.Label(header, text=f"Scanning: {DOWNLOADS}", font=("Segoe UI", 9),
         bg="#1E293B", fg="#94A3B8").pack(anchor="w", pady=(2, 0))

# ── Cards ─────────────────────────────────────────────────────────────────
cards_frame = tk.Frame(root, bg="#F8F9FA", padx=16, pady=14)
cards_frame.pack(fill=tk.BOTH, expand=True)

for i, rule in enumerate(RULES):
    card = tk.Frame(cards_frame, bg="white", relief=tk.FLAT,
                    highlightbackground="#E2E8F0", highlightthickness=1)
    card.pack(fill=tk.X, pady=(0, 12))

    # Card header
    card_top = tk.Frame(card, bg=rule["light"], padx=12, pady=8)
    card_top.pack(fill=tk.X)

    tag_badge = tk.Label(card_top, text=rule["tag"],
                         font=("Segoe UI", 10, "bold"),
                         bg=rule["color"], fg="white",
                         padx=8, pady=2)
    tag_badge.pack(side=tk.LEFT)

    tk.Label(card_top, text=f"→  {rule['folder']}",
             font=("Segoe UI", 10), bg=rule["light"], fg="#334155").pack(side=tk.LEFT, padx=10)

    count_lbl = tk.Label(card_top, text="", font=("Segoe UI", 9),
                          bg=rule["light"], fg=rule["color"])
    count_lbl.pack(side=tk.RIGHT)
    rule["count"] = count_lbl

    # File list
    lb_frame = tk.Frame(card, bg="white")
    lb_frame.pack(fill=tk.X, padx=10, pady=8)

    sb = tk.Scrollbar(lb_frame, orient=tk.VERTICAL)
    lb = tk.Listbox(lb_frame, font=("Segoe UI", 9), height=5,
                    bg="white", fg="#1E293B", bd=0, highlightthickness=0,
                    selectbackground=rule["light"], selectforeground="#1E293B",
                    yscrollcommand=sb.set)
    sb.config(command=lb.yview)
    lb.pack(side=tk.LEFT, fill=tk.X, expand=True)
    sb.pack(side=tk.RIGHT, fill=tk.Y)
    rule["listbox"] = lb

# ── Bottom bar ────────────────────────────────────────────────────────────
bottom = tk.Frame(root, bg="#F1F5F9", padx=16, pady=12)
bottom.pack(fill=tk.X, side=tk.BOTTOM)

status_lbl = tk.Label(bottom, textvariable=status_var, font=("Segoe UI", 9),
                      bg="#F1F5F9", fg="#64748B", wraplength=320, justify=tk.LEFT)
status_lbl.pack(side=tk.LEFT)

btn_frame = tk.Frame(bottom, bg="#F1F5F9")
btn_frame.pack(side=tk.RIGHT)

scan_btn = tk.Button(btn_frame, text="Scan", command=scan,
                     font=("Segoe UI", 10), bg="white", fg="#1E293B",
                     relief=tk.FLAT, padx=16, pady=7, cursor="hand2",
                     highlightbackground="#CBD5E1", highlightthickness=1)
scan_btn.pack(side=tk.LEFT, padx=(0, 8))

move_btn = tk.Button(btn_frame, text="Move All →", command=move_all,
                     font=("Segoe UI", 10, "bold"), bg="#1E293B", fg="white",
                     relief=tk.FLAT, padx=16, pady=7, cursor="hand2",
                     state=tk.DISABLED)
move_btn.pack(side=tk.LEFT)

root.mainloop()
