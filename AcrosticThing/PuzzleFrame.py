import tkinter as tk
from GridEntry import GridEntry


class PuzzleFrame(tk.Frame):
    def __init__(self, master, rows=8, columns=23, **kwargs):
        super().__init__(master, **kwargs)  ##if one does not put in a parent widget, 'master' in this case, it defaults to the root window

        self.master = master
        self.rows = rows
        self.columns = columns
        self.boxes = []
        self.generate_boxes()
        self.bind_events()

        self.pack()

    @classmethod
    def from_entry_list(cls, master, rows, columns, entry_list):
        puzzle_grid = cls(master, rows, columns)
        for i in range(len(entry_list)):
            box = puzzle_grid.boxes[i]
            box.configure(state=entry_list[i], disabledbackground='black')
            box.unbind('<Button-3>')

        puzzle_grid.renumber_grid()

        return puzzle_grid

    @classmethod
    def from_clue_frame(cls, master, rows, columns, idk):
        puzzle_grid = cls(master, rows, columns)

    def bind_events(self):
        for box in self.boxes:
            box.set_binding('<Enter>', 'toggle_highlight')
            box.set_binding('<Leave>', 'toggle_highlight')
            box.set_binding('<Button-3>', 'toggle_state')
            # box.bind('<Enter>', self.toggle_box_highlight)
            # box.bind('<Leave>', self.toggle_box_highlight)
            # box.bind('<Button-3>', self.toggle_box_state)

    def generate_boxes(self, entry_list=None):
        grid_num = 1
        if not entry_list:
            for r in range(1, self.rows+1):
                for c in range(1, self.columns+1):
                    colors = {'bg': 'blue', 'fg': 'white', 'highlight': 'red', 'unhighlight': 'blue'}
                    e = GridEntry(self, colors=colors, width=5)
                    e.grid(row=r, column=c, sticky='nsew')
                    self.boxes.append(e)
                    grid_num += 1

            for i in range(self.rows):
                tk.Grid.rowconfigure(self, i, weight=1)

            for i in range(self.columns):
                tk.Grid.columnconfigure(self, i, weight=1)
        else:
            for r in range(1, self.rows+1):
                for c in range(1, self.columns+1):
                    pass

    def get_enabled_boxes(self):
        enabled_boxes = [box for box in self.boxes if box['state'] == 'normal']
        enabled_dict = dict(enumerate(enabled_boxes, 1))
        return enabled_dict


    def renumber_grid(self):
        num = 1
        for box in self.boxes:
            if box['state'] == 'normal':
                box.grid_num = num
                num += 1

    def toggle_box_highlight(self, event=None):
        box = event.widget
        if box['bg'] == 'blue':
            box.configure(bg='red')
            # print(f'entering grid display box#: {box.grid_num}')
        else:
            box.configure(bg='blue')
            # print(f'leaving grid display box#: {box.grid_num}')

        return 'break'

    def reset_layout(self):
        for box in self.boxes:
            box.delete(0, tk.END)

    def highlight_box(self, event):
        box = event.widget
        box.configure(bg='red')

        return 'break'  # this prevents the event from percolating up to the master widget

    def unhighlight_box(self, event):
        box = event.widget
        box.configure(bg='blue')

        return 'break'

    def toggle_box_state(self, event=None):
        box = event.widget
        if box['state'] == 'normal':
            box.configure(state='disabled', disabledbackground='black')
        else:
            box.configure(state='normal')

        return 'break'


if __name__ == '__main__':
    win = tk.Tk()
    win.title('boingus')
    h = tk.Toplevel(win)
    h.title('gloink')
    pg = PuzzleFrame(h)
    win.mainloop()