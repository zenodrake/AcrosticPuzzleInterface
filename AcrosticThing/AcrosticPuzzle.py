import tkinter as tk
import tkinter.ttk as ttk
from functools import partial


from PuzzleFrame import PuzzleFrame
from ClueFrame import ClueFrame
from EnterNewPuzzleWindow import EnterNewPuzzleWindow

# TODO: we don't apparently need to return a dictionary for the get_answer_cells()
#  or get_enabled_cells() functions. change them to lists?
# TODO: make a new parent class for PuzzleFrame and ClueDisplay as they seem to share a lot of code
# TODO: clean up the link_clues() function. not sure how it should be cleaner, but it needs to be cleaner
# TODO:



class AcrosticPuzzle(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title('Acrostic Thing For Learning')
        self.geometry('1000x1000')
        self.menu = tk.Menu(self, bg='grey', fg='black')

        self.menu.add_command(label='New Game', command=self.new_game)
        self.menu.add_command(label='Reset Game', command=self.reset_game)
        self.menu.add_command(label='Remove game', command=self.remove_game)

        self.puzzle_frame = tk.Frame(self)
        self.clue_frame = tk.Frame(self)
        self.puzzle_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.clue_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.enabled_grid_dict = None
        self.clue_answers_dict = None
        self.configure(menu=self.menu)

    def link_clues(self):
        self.enabled_grid_dict = self.puzzle_frame.get_enabled_cells()
        self.clue_answers_dict = self.clue_frame.get_answer_cells()

        for ce, ge in zip(self.clue_answers_dict.values(), self.enabled_grid_dict.values()):
            grid_num = int(ce.grid_num)
            sv = tk.StringVar()
            ge.configure(textvar=sv)
            ce.configure(textvar=sv)

            ge.clear_bindings()
            ce.clear_bindings()

            ge.set_binding('<Enter>', 'toggle_highlight')
            ce.set_binding('<Enter>', 'toggle_highlight')
            ge.set_binding('<Leave>', 'toggle_highlight')
            ce.set_binding('<Leave>', 'toggle_highlight')

            ge.bind('<Enter>', lambda e, g=grid_num: self.highlight_clue_cell(g))
            ge.bind('<Leave>', lambda e, g=grid_num: self.unhighlight_clue_cell(g))
            ce.bind('<Enter>', lambda e, g=grid_num: self.highlight_grid_cell(g))
            ce.bind('<Leave>', lambda e, g=grid_num: self.unhighlight_grid_cell(g))

        h = self.clue_frame.get_clue_labels()

        def highlight_grid_cells(grid_nums):
            for num in map(int, grid_nums):
                cell = self.enabled_grid_dict[num]
                cell.configure(bg='yellow')

        def unhighlight_grid_cells(grid_nums):
            for num in map(int, grid_nums):
                cell = self.enabled_grid_dict[num]
                cell.configure(bg='blue')

        for k, v in h.items():
            k.bind('<Enter>', lambda e, grid_nums=v: highlight_grid_cells(grid_nums))
            k.bind('<Leave>', lambda e, grid_nums=v: unhighlight_grid_cells(grid_nums))

    def highlight_grid_cell(self, grid_num):
        cell = self.enabled_grid_dict[grid_num]
        cell.configure(bg='yellow')
        return 'break'

    def unhighlight_grid_cell(self, grid_num):
        cell = self.enabled_grid_dict[grid_num]
        cell.configure(bg='blue')
        return 'break'

    def highlight_clue_cell(self, grid_num):
        cell = self.clue_answers_dict[grid_num]
        cell.configure(bg='yellow')
        return 'break'

    def unhighlight_clue_cell(self, grid_num):
        cell = self.clue_answers_dict[grid_num]
        cell.configure(bg='white')
        return 'break'

    def new_game(self):
        """Erase everything and prompt the user for a new setup"""
        if self.puzzle_frame:
            self.puzzle_frame.pack_forget()
        if self.clue_frame:
            self.clue_frame.pack_forget()

        puzzle = EnterNewPuzzleWindow(self)

        # wait_window pauses execution of the next line until the window is destroyed
        self.wait_window(puzzle)
        puzzle_info = puzzle.puzzle_dict

        if puzzle_info:
            rows, columns = puzzle_info['rows'], puzzle_info['cols']
            grid_states = puzzle_info['grid_states']
            clue_list = puzzle_info['clue_list']
            self.puzzle_frame = PuzzleFrame.from_entry_list(self, rows, columns, grid_states)
            self.clue_frame = ClueFrame(self, clue_list)
            self.clue_frame.enable_clue_entries()
            self.link_clues()

    def remove_game(self):
        self.puzzle_frame.pack_forget()
        self.clue_frame.pack_forget()

    def reset_game(self):
        """Clear everything from all cells, both in the puzzle frame and the clue frame"""
        self.puzzle_frame.reset_layout()
        self.clue_frame.reset_layout()


def main():
    puzz = AcrosticPuzzle()
    puzz.mainloop()


if __name__ == '__main__':
    p = AcrosticPuzzle()
    p.mainloop()