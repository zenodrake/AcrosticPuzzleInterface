import tkinter as tk

from AnswerCellDisplay import AnswerCellDisplay
from GridEntry import GridEntry
"""A ClueDisplay consists of the following elements
    1. The clue indicator and text. Indicator is a letter (A, B, C, ...). How many kilometers is a parsec?
    3. The clue answer, when initialized, blank cells.

    The clue letter and text is a tk.Label. Format is like "A. What is your name?" or "H. What is your favorite color?"
    The clue answer is a series of tk.Entries
    
"""


class ClueDisplay(AnswerCellDisplay):
    def __init__(self, master, clue_text, grid_numbers, **kwargs):
        self.clue_text = clue_text
        self.grid_numbers = grid_numbers
        super().__init__(master, **kwargs)
        self.clue_label = tk.Label(self, text=clue_text, fg='black', bg='white')
        self.clue_label.grid(row=1, column=1, padx=(0, 5))

    def enable_entries(self):
        for cell in self.answer_cells:
            cell['state'] = 'normal'

    def generate_answer_cells(self):
        for c, gn in enumerate(self.grid_numbers, 2):
            colors = {'bg': 'white', 'fg': 'black', 'highlight': 'LightSkyBlue', 'unhighlight': 'white'}
            answer_cell = GridEntry(self, grid_num=gn, colors=colors, width=5)
            answer_cell.grid(row=1, column=c, padx=(2, 2))
            self.answer_cells.append(answer_cell)

    def get_clue_label(self):
        return {self.clue_label: self.grid_numbers}

    def setup_label_highlight(self, grid_numbers):
        pass

if __name__ == '__main__':
    win = tk.Tk()
    clue = 'thingus'
    numbers = [1, 2, 3]
    cd = ClueDisplay(win, clue, numbers)
    # cd.pack()
    win.mainloop()