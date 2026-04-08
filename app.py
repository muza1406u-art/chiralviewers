"""Tkinter app for exploring Artemether stereocentres and CIP priorities."""

import tkinter as tk
from tkinter import ttk

STEREOCENTRES = [
    {
        "pos": "C-3",
        "config": "R",
        "desc": "Methyl-bearing carbon in the lactone ring.",
        "subs": [
            ("O (ring)", 1),
            ("O (peroxide)", 2),
            ("CH2 (ring)", 3),
            ("CH3", 4),
        ],
    },
    {
        "pos": "C-5a",
        "config": "S",
        "desc": "Ring junction carbon.",
        "subs": [
            ("O (ring)", 1),
            ("C-6", 2),
            ("C-5", 3),
            ("H", 4),
        ],
    },
    {
        "pos": "C-6",
        "config": "R",
        "desc": "Cyclohexane ring carbon.",
        "subs": [
            ("C-5a", 1),
            ("C-7", 2),
            ("CH3", 3),
            ("H", 4),
        ],
    },
]


def build_app() -> tk.Tk:
    """Create and return the main tkinter window."""
    root = tk.Tk()
    root.title("Artemether Chirality Explorer")
    root.geometry("760x460")

    main = ttk.Frame(root, padding=12)
    main.pack(fill="both", expand=True)

    left_frame = ttk.Frame(main)
    left_frame.pack(side="left", fill="y", padx=(0, 12))

    right_frame = ttk.Frame(main)
    right_frame.pack(side="right", fill="both", expand=True)

    ttk.Label(left_frame, text="Stereocentres", font=("Arial", 11, "bold")).pack(anchor="w", pady=(0, 6))

    listbox = tk.Listbox(left_frame, width=24, height=18)
    listbox.pack(fill="y")

    for centre in STEREOCENTRES:
        listbox.insert(tk.END, f"{centre['pos']} ({centre['config']})")

    title_label = ttk.Label(right_frame, text="Select a stereocentre", font=("Arial", 14, "bold"))
    title_label.pack(anchor="w")

    desc_label = ttk.Label(right_frame, text="", wraplength=460, justify="left")
    desc_label.pack(anchor="w", pady=(8, 8))

    subs_label = ttk.Label(right_frame, text="", justify="left")
    subs_label.pack(anchor="w")

    def show_details(_event: tk.Event) -> None:
        selected = listbox.curselection()
        if not selected:
            return

        centre = STEREOCENTRES[selected[0]]
        title_label.config(text=f"{centre['pos']} — {centre['config']}")
        desc_label.config(text=centre["desc"])

        subs_text = "CIP Priorities:\n"
        for substituent, priority in centre["subs"]:
            subs_text += f"{priority}. {substituent}\n"
        subs_label.config(text=subs_text)

    listbox.bind("<<ListboxSelect>>", show_details)

    listbox.selection_set(0)
    listbox.event_generate("<<ListboxSelect>>")

    return root


if __name__ == "__main__":
    app = build_app()
    app.mainloop()
