import tkinter as tk

from AnswerCellDisplay import AnswerCellDisplay
from GridEntry import GridEntry


class PuzzleFrame(AnswerCellDisplay):
    def __init__(self, master, rows=8, columns=23, **kwargs):
        self.rows = rows
        self.columns = columns
        super().__init__(master, **kwargs)
        self.pack()

    @classmethod
    def from_entry_list(cls, master, rows, columns, entry_list):
        puzzle_grid = cls(master, rows, columns)
        for i in range(len(entry_list)):
            box = puzzle_grid.answer_cells[i]
            box.configure(state=entry_list[i], disabledbackground='black')
            box.unbind('<Button-3>')

        puzzle_grid.renumber_grid()

        return puzzle_grid

    @classmethod
    def from_clue_frame(cls, master, rows, columns, idk):
        puzzle_grid = cls(master, rows, columns)

    def allow_focus_traversal(self, event=None):
        self.configure(takefocus=1)
        for cell in self.answer_cells:
            cell.configure(takefocus=1)

    def deny_focus_traversal(self, event=None):
        self.configure(takefocus=0)
        for cell in self.answer_cells:
            cell.configure(takefocus=0)

    def bind_events(self):
        super().bind_events()
        for cell in self.answer_cells:
            cell.set_binding('<Button-3>', 'toggle_state')

    def generate_answer_cells(self, entry_list=None):
        grid_num = 1
        if not entry_list:
            for r in range(1, self.rows+1):
                for c in range(1, self.columns+1):
                    colors = {'bg': 'blue', 'fg': 'white', 'highlight': 'red', 'unhighlight': 'blue'}
                    e = GridEntry(self, colors=colors, width=5)
                    e.grid(row=r, column=c, sticky='nsew')
                    self.answer_cells.append(e)
                    grid_num += 1

            for i in range(self.rows):
                tk.Grid.rowconfigure(self, i, weight=1)

            for i in range(self.columns):
                tk.Grid.columnconfigure(self, i, weight=1)
        else:
            for r in range(1, self.rows+1):
                for c in range(1, self.columns+1):
                    pass

    def get_enabled_cells(self):
        enabled_cells = [cell for cell in self.answer_cells if cell['state'] == 'normal']
        enabled_dict = dict(enumerate(enabled_cells, 1))
        return enabled_dict

    def renumber_grid(self):
        num = 1
        for cell in self.answer_cells:
            if cell['state'] == 'normal':
                cell.grid_num = num
                num += 1

    def toggle_cell_highlight(self, event=None):
        cell = event.widget
        if cell['bg'] == 'blue':
            cell.configure(bg='red')
            # print(f'entering grid display box#: {box.grid_num}')
        else:
            cell.configure(bg='blue')
            # print(f'leaving grid display box#: {box.grid_num}')

        return 'break'

    def reset_layout(self):
        for cell in self.answer_cells:
            cell.delete(0, tk.END)

    def highlight_box(self, event):
        cell = event.widget
        cell.configure(bg='red')

        return 'break'  # this prevents the event from percolating up to the master widget

    def unhighlight_box(self, event):
        cell = event.widget
        cell.configure(bg='blue')

        return 'break'

    def toggle_cell_state(self, event=None):
        cell = event.widget
        if cell['state'] == 'normal':
            cell.configure(state='disabled', disabledbackground='black')
        else:
            cell.configure(state='normal')

        return 'break'


if __name__ == '__main__':
    win = tk.Tk()
    win.title('boingus')
    # h = tk.Toplevel(win)
    # h.title('gloink')
    pg = PuzzleFrame(win)
    win.mainloop()