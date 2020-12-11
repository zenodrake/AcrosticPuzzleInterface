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

        return puzzle_grid

    def generate_boxes(self):
        grid_num = 1
        for r in range(1, self.rows+1):
            for c in range(1, self.columns+1):
                # e = tk.Entry(self, bg='blue', width=5)

                e = GridEntry(self, grid_num, bg='blue', width=5)
                e.grid(row=r, column=c, sticky='nsew')
                self.boxes.append(e)
                grid_num += 1

        for i in range(self.rows):
            tk.Grid.rowconfigure(self, i, weight=1)

        for i in range(self.columns):
            tk.Grid.columnconfigure(self, i, weight=1)


    def bind_events(self):
        for box in self.boxes:
            box.bind('<Enter>', self.toggle_box_highlight)
            box.bind('<Leave>', self.toggle_box_highlight)
            box.bind('<Button-3>', self.toggle_box_state)
            # box.bind('<Button-1>', lambda e: print(e.widget))

    def toggle_box_highlight(self, event=None):
        box = event.widget
        if box['bg'] == 'blue':
            box.configure(bg='red')
        else:
            box.configure(bg='blue')

        return 'break'


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