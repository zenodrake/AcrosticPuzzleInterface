import tkinter as tk

"""A ClueDisplay consists of the following elements
    1. The clue indicator and text. Indicator is a letter (A, B, C, ...). How many kilometers is a parsec?
    3. The clue answer, when initialized, blank cells.

    The clue letter and text is a tk.Label. Format is like "A. What is your name?" or "H. What is your favorite color?"
    The clue answer is a series of tk.Entries
    
"""

class ClueDisplay(tk.Frame):
    def __init__(self, master, clue_text, entry_numbers, **kwargs):
        super().__init__(master, **kwargs)

        self.master = master
        self.clue_text = clue_text
        self.entry_numbers = entry_numbers
        self.entries = []
        clue_label = tk.Label(self, text=clue_text, fg='black', bg='white').grid(row=1, column=1, padx=(0, 5))

        for c, i in enumerate(self.entry_numbers, 2):
            entry = tk.Entry(self, textvar=tk.StringVar(), bg='white', width=5)
            entry.grid(row=1, column=c, padx=(2, 2))
            self.entries.append(entry)

        self.bind_events()

    def bind_events(self):
        # Not sure how to tie these into the PuzzleFrame entries, but will figure that out
        for entry in self.entries:
            entry.bind('<Enter>', self.toggle_box_highlight)
            entry.bind('<Leave>', self.toggle_box_highlight)


    def toggle_box_highlight(self, event=None):
        box = event.widget
        if box['bg'] == 'white':
            box.configure(bg='LightSkyBlue')
        else:
            box.configure(bg='white')

        return 'break'