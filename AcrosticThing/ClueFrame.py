import tkinter as tk


class ClueFrame(tk.Frame):
    def __init__(self, master, clue_dict, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.clue_dict = clue_dict
        self.configure(bg='green')

        # label = tk.Label(self, text='Thingus')
        # label.pack(side=tk.LEFT, fill=tk.X, expand=True)



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

        num_clues = len(self.clue_dict)
        for k, v in self.clue_dict.items():
            label_text = chr(int(k)+64) + '. '
            clue_text = v[0]
            entry_numbers = v[1]

            # create a frame to hold each clue. this frame will hold the Label with the clue text
            # and however many entries are necessary for the answer
            clue_frame = tk.Frame(self, bg='green')
            clue_label = tk.Label(clue_frame, text=label_text + clue_text, fg='black', bg='white')

            # grid_row = 0
            # grid_col = 0
            if k < 14:
                grid_row = k
                grid_col = 1

            else:
                grid_row = k-13
                grid_col = 2

            clue_frame.grid(row=grid_row, column=grid_col, sticky='w', padx=(5, 10))  #when padx (or pady) is passed a tuple, the left value controls padding on the left, right on the right
            clue_label.grid(row=1, column=0, padx=(0, 5))
            for c, i in enumerate(entry_numbers, 2):
                entry = tk.Entry(clue_frame, textvar=tk.StringVar(), bg='white', width=5)
                entry.grid(row=1, column=c, padx=(2, 2))
            # tk.Grid.rowconfigure(clue_frame, grid_row, weight=1)
            # tk.Grid.columnconfigure(clue_frame, grid_col, weight=1)



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
        24: ('mountani-biking slang', [1, 2, 4]),
        25: ('the last clue', [1, 2, 4])
    }
    cf = ClueFrame(win, sample_dict)
    win.mainloop()