import tkinter as tk
from ClueDisplay import ClueDisplay

class ClueFrame(tk.Frame):
    """clue_dict should be formatted thusly: {int: (str, []), ...}"""
    def __init__(self, master, clue_dict, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.clue_dict = clue_dict
        self.configure(bg='green')

        self.sample_dict = {
                1: ('john sayles western', [1, 2, 3]),
                2: ('bowled over', [8, 33, 12]),
                3: ('chief joseph', [46, 78, 12, 13]),
                4: ('an early work', [12, 13, 14]),
                5: ('april 22, since 1970', [1, 2, 4]),
                6: ('focus of a museum', [1, 2, 3]),
                7: ('author of absurdist plays', [1, 2, 4]),
                8: ('ophthalmologist snellen invention', [1, 2, 4]),
                9: ('twiggy or iman', [1, 2, 4]),
                10: ('firefighter in a remote area', [1, 2, 4]),
                11: ('collectible toy vehicle', [1, 2, 4]),
                12: ('prolific swiss mathematician', [1, 2, 4]),
                13: ('simon and garfunkel hit', [1, 2, 4]),
                14: ('tourist locale', [1, 2, 4]),
                15: ('winged ball pursuit', [1, 2, 4]),
                16: ('asteroid', [1, 2, 4]),
                17: ('cleft stick carried by clotho', [1, 2, 4]),
                18: ('alto saxophone', [1, 2, 4]),
                19: ('engine for a boeing 707', [1, 2, 4]),
                20: ('laughable blunder; very funny joke', [1, 2, 4]),
                21: ('legendary corrida showman', [1, 2, 4]),
                22: ('era of mood rings', [1, 2, 4]),
                23: ('determinant of destiny in jainism', [1, 2, 4]),
                24: ('mountain-biking slang', [1, 2, 4]),
                25: ('the last clue', [1, 2, 4])
            }

        self.layout_clues()
        self.pack(expand=True, fill=tk.BOTH)

    def layout_clues(self):
        if not self.clue_dict:
            self.clue_dict = self.sample_dict

        # num_clues = len(self.clue_dict)
        for k, v in self.clue_dict.items():
            label_text = chr(int(k)+64) + '. '
            clue_text = v[0]
            entry_numbers = v[1]
            clue = ClueDisplay(self, label_text + clue_text, entry_numbers, bg='green')

            if k < 14:
                grid_row = k
                grid_col = 1

            else:
                grid_row = k-13
                grid_col = 2

            clue.grid(row=grid_row, column=grid_col, sticky='w', padx=(5, 10))

    def update_clue_layout(self, new_clue):
        if self.clue_dict == self.sample_dict:
            self.clue_dict = {}
        self.clue_dict.update(new_clue)
        self.layout_clues()


if __name__ == '__main__':
    win = tk.Tk()
    sample_dict = {
        1: ('john sayles western', [1, 2, 3]),
        2: ('bowled over', [8, 33, 12]),
        3: ('chief joseph', [46, 78, 12, 13]),
        4: ('an early work', [12, 13, 14]),
        5: ('april 22, since 1970', [1, 2, 4]),
        6: ('focus of a museum', [1, 2, 3]),
        7: ('author of absurdist plays', [1, 2, 4]),
        8: ('ophthalmologist snellen invention', [1, 2, 4]),
        9: ('twiggy or iman', [1, 2, 4]),
        10: ('firefighter in a remote area', [1, 2, 4]),
        11: ('collectible toy vehicle', [1, 2, 4]),
        12: ('prolific swiss mathematician', [1, 2, 4]),
        13: ('simon and garfunkel hit', [1, 2, 4]),
        14: ('tourist locale', [1, 2, 4]),
        15: ('winged ball pursuit', [1, 2, 4]),
        16: ('asteroid', [1, 2, 4]),
        17: ('cleft stick carried by clotho', [1, 2, 4]),
        18: ('alto saxophone', [1, 2, 4]),
        19: ('engine for a boeing 707', [1, 2, 4]),
        20: ('laughable blunder; very funny joke', [1, 2, 4]),
        21: ('legendary corrida showman', [1, 2, 4]),
        22: ('era of mood rings', [1, 2, 4]),
        23: ('determinant of destiny in jainism', [1, 2, 4]),
        24: ('mountain-biking slang', [1, 2, 4]),
        25: ('the last clue', [1, 2, 4])
    }
    cf = ClueFrame(win, sample_dict)
    win.mainloop()