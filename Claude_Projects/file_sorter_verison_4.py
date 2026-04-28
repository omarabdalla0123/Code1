import os
import shutil
import tkinter as tk
from tkinter import messagebox

DOWNLOADS = os.path.join(os.path.expanduser("~"), "Downloads")

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".bmp", ".tiff", ".ico", ".raw"}

TAG_RULES = [
    {"label": "(PT)", "tag": "(PT)", "folder": "product tamples", "color": "#2563EB", "light": "#EFF6FF", "count": None, "listbox": None},
    {"label": "(CF)", "tag": "(CF)", "folder": "CF_Files",         "color": "#059669", "light": "#ECFDF5", "count": None, "listbox": None},
    {"label": "(OM)", "tag": "(OM)", "folder": "Old Menu",          "color": "#D97706", "light": "#FFFBEB", "count": None, "listbox": None},
]

img_rule = {
    "folder": "Logos Photos",
    "color": "#9333EA",
    "light": "#FAF5FF",
    "count": None,
    "listbox": None,
}

def scan():
    for rule in TAG_RULES:
        rule["listbox"].delete(0, tk.END)
        rule["count"].config(text="")
    img_rule["listbox"].delete(0, tk.END)
    img_rule["count"].config(text="")

    total = 0
    for filename in os.listdir(DOWNLOADS):
        filepath = os.path.join(DOWNLOADS, filename)
        if not os.path.isfile(filepath):
            continue
        name, ext = os.path.splitext(filename)
        name_stripped = name.strip()

        matched_tag = False
        for rule in TAG_RULES:
            if name_stripped.endswith(rule["tag"]):
                rule["listbox"].insert(tk.END, "  " + filename)
                total += 1
                matched_tag = True
                break

        if not matched_tag and ext.lower() in IMAGE_EXTS:
            img_rule["listbox"].insert(tk.END, "  " + filename)
            total += 1

    for rule in TAG_RULES:
        n = rule["listbox"].size()
        rule["count"].config(text=f"{n} file{'s' if n != 1 else ''}")

    n_img = img_rule["listbox"].size()
    img_rule["count"].config(text=f"{n_img} file{'s' if n_img != 1 else ''}")

    move_btn.config(state=tk.NORMAL if total > 0 else tk.DISABLED)
    status_var.set(f"Found {total} file(s) ready to sort." if total else "No matching files found in Downloads.")

def move_all():
    moved = 0
    errors = []

    for rule in TAG_RULES + [img_rule]:
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

# ── Window ───────────────────────────────────────────────────────────────
root = tk.Tk()
root.title("File Sorter")
root.geometry("540x780")
root.resizable(False, False)
root.configure(bg="#F8F9FA")

status_var = tk.StringVar(value="Click Scan to detect files in your Downloads folder.")

# ── Header ────────────────────────────────────────────────────────────────
header = tk.Frame(root, bg="#1E293B", padx=20, pady=16)
header.pack(fill=tk.X)

tk.Label(header, text="File Sorter", font=("Segoe UI", 15, "bold"),
         bg="#1E293B", fg="white").pack(anchor="w")
tk.Label(header, text=f"Scanning: {DOWNLOADS}", font=("Segoe UI", 9),
         bg="#1E293B", fg="#94A3B8").pack(anchor="w", pady=(2, 0))

# ── Cards ─────────────────────────────────────────────────────────────────
cards_frame = tk.Frame(root, bg="#F8F9FA", padx=16, pady=14)
cards_frame.pack(fill=tk.BOTH, expand=True)

def make_card(parent, rule, badge_text):
    card = tk.Frame(parent, bg="white", relief=tk.FLAT,
                    highlightbackground="#E2E8F0", highlightthickness=1)
    card.pack(fill=tk.X, pady=(0, 10))

    card_top = tk.Frame(card, bg=rule["light"], padx=12, pady=8)
    card_top.pack(fill=tk.X)

    tk.Label(card_top, text=badge_text,
             font=("Segoe UI", 10, "bold"),
             bg=rule["color"], fg="white",
             padx=8, pady=2).pack(side=tk.LEFT)

    tk.Label(card_top, text=f"  →  {rule['folder']}",
             font=("Segoe UI", 10), bg=rule["light"], fg="#334155").pack(side=tk.LEFT)

    count_lbl = tk.Label(card_top, text="", font=("Segoe UI", 9),
                         bg=rule["light"], fg=rule["color"])
    count_lbl.pack(side=tk.RIGHT)
    rule["count"] = count_lbl

    lb_frame = tk.Frame(card, bg="white")
    lb_frame.pack(fill=tk.X, padx=10, pady=8)

    sb = tk.Scrollbar(lb_frame, orient=tk.VERTICAL)
    lb = tk.Listbox(lb_frame, font=("Segoe UI", 9), height=3,
                    bg="white", fg="#1E293B", bd=0, highlightthickness=0,
                    selectbackground=rule["light"], selectforeground="#1E293B",
                    yscrollcommand=sb.set)
    sb.config(command=lb.yview)
    lb.pack(side=tk.LEFT, fill=tk.X, expand=True)
    sb.pack(side=tk.RIGHT, fill=tk.Y)
    rule["listbox"] = lb

for rule in TAG_RULES:
    make_card(cards_frame, rule, rule["label"])

make_card(cards_frame, img_rule, "Images (.jpg .png .svg ...)")

# ── Bottom bar ────────────────────────────────────────────────────────────
bottom = tk.Frame(root, bg="#F1F5F9", padx=16, pady=12)
bottom.pack(fill=tk.X, side=tk.BOTTOM)

status_lbl = tk.Label(bottom, textvariable=status_var, font=("Segoe UI", 9),
                      bg="#F1F5F9", fg="#64748B", wraplength=300, justify=tk.LEFT)
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
