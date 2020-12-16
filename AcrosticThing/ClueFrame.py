import tkinter as tk
from ClueDisplay import ClueDisplay


class ClueFrame(tk.Frame):
    """clue_dict should be formatted thusly: {int: (str, []), ...}"""
    def __init__(self, master, clue_list=None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.clue_list = clue_list
        self.clue_answers = []
        self.configure(bg='green')

        self.sample_clues = [
                ['john sayles western', [1, 2, 3]],
                ['bowled over', [8, 33, 12]],
                ['chief joseph', [46, 78, 12, 13]],
                ['an early work', [12, 13, 14]],
                ['april 22, since 1970', [1, 2, 4]],
                ['focus of a museum', [1, 2, 3]],
                ['author of absurdist plays', [1, 2, 4]],
                ['ophthalmologist snellen invention', [1, 2, 4]],
                ['twiggy or iman', [1, 2, 4]],
                ['firefighter in a remote area', [1, 2, 4]],
                ['collectible toy vehicle', [1, 2, 4]],
                ['prolific swiss mathematician', [1, 2, 4]],
                ['simon and garfunkel hit', [1, 2, 4]],
                ['tourist locale', [1, 2, 4]],
                ['winged ball pursuit', [1, 2, 4]],
                ['asteroid', [1, 2, 4]],
                ['cleft stick carried by clotho', [1, 2, 4]],
                ['alto saxophone', [1, 2, 4]],
                ['engine for a boeing 707', [1, 2, 4]],
                ['laughable blunder; very funny joke', [1, 2, 4]],
                ['legendary corrida showman', [1, 2, 4]],
                ['era of mood rings', [1, 2, 4]],
                ['determinant of destiny in jainism', [1, 2, 4]],
                ['mountain-biking slang', [1, 2, 4]],
                ['the last clue', [1, 2, 4]]
            ]

        self.layout_clues()
        self.pack(expand=True, fill=tk.BOTH)

    def enable_clue_entries(self):
        for clue in self.clue_answers:
            clue.enable_entries()

    def get_clue_entries(self):
        entries = []
        for clue in self.clue_answers:
            entries += clue.entries

        entries_dict = dict(zip([int(entry.grid_num) for entry in entries], entries))
        return entries_dict

    def layout_clues(self):
        if not self.clue_list:
            self.clue_list = self.sample_clues

        for i, v in enumerate(self.clue_list, 1):
            label_text = chr(i+64) + '. '
            clue_text = v[0]
            answer_spaces = v[1]
            clue_answer = ClueDisplay(self, label_text + clue_text, answer_spaces, bg='green')

            if i < 14:
                grid_row = i
                grid_col = 1
            else:
                grid_row = i - 13
                grid_col = 2

            clue_answer.grid(row=grid_row, column=grid_col, sticky='w', padx=(5, 10))
            self.clue_answers.append(clue_answer)

    def reset_layout(self):
        for clue in self.clue_answers:
            clue.reset_entries()

    def update_clue_layout(self, new_clue):
        if self.clue_list == self.sample_clues:
            self.clue_list = []
        self.clue_list.append(new_clue)
        self.layout_clues()


if __name__ == '__main__':
    win = tk.Tk()
    cf = ClueFrame(win)
    # menu = tk.Menu(win)
    # menu.add_command(label='push me', command=cf.show_sorted)
    # win.configure(menu=menu)
    win.mainloop()
