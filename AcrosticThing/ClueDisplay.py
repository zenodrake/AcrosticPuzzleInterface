import tkinter as tk

from GridEntry import GridEntry
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

        for c, gn in enumerate(self.entry_numbers, 2):
            colors = {'bg': 'white', 'fg': 'black', 'highlight': 'LightSkyBlue', 'unhighlight': 'white'}
            entry = GridEntry(self, grid_num=gn, colors=colors, width=5)
            entry.grid(row=1, column=c, padx=(2, 2))
            self.entries.append(entry)

        self.bind_events()

    def bind_events(self):
        # Not sure how to tie these into the PuzzleFrame entries, but will figure that out
        for entry in self.entries:
            entry.set_binding('<Enter>', 'toggle_highlight')
            entry.set_binding('<Leave>', 'toggle_highlight')
            entry.bind('<KeyRelease>', self.focus_next_entry)
        self.bind('<Enter>', lambda u: print('thingus'))

    def enable_entries(self):
        for entry in self.entries:
            entry['state'] = 'normal'

    def focus_next_entry(self, event=None):
        passable_events = ['Tab', 'BackSpace', 'Delete']
        if event.keysym in passable_events:
            pass
        else:
            curr_entry = event.widget
            next_entry = curr_entry.tk_focusNext()
            next_entry.focus()
            next_entry.selection_range(0, tk.END)





    def reset_entries(self):
        for entry in self.entries:
            entry.delete(0, tk.END)

    def toggle_box_highlight(self, event=None):
        box = event.widget
        if box['bg'] == 'white':
            box.configure(bg='LightSkyBlue')
            # print(f'entering clue display box#: {box.grid_num}')
        else:
            box.configure(bg='white')
            # print(f'leaving clue display box#: {box.grid_num}')

        return 'break'


if __name__ == '__main__':
    win = tk.Tk()
    clue = 'thingus'
    numbers = [1,2,3]
    cd = ClueDisplay(win, clue, numbers)
    cd.pack()
    win.mainloop()