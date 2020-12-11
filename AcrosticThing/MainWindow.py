import tkinter as tk
import tkinter.ttk as ttk

from PuzzleFrame import PuzzleFrame
from ClueFrame import ClueFrame
from EnterNewPuzzleWindow import EnterNewPuzzleWindow


class MainWindow(tk.Tk):
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

        self.configure(menu=self.menu)


    def new_game(self):
        """Erase everything and prompt the user for a new setup"""
        if self.puzzle_frame:
            self.puzzle_frame.pack_forget()

        puzzle = EnterNewPuzzleWindow(self)

        # wait_window pauses execution of the next line until the window is destroyed
        self.wait_window(puzzle)
        puzzle_info = puzzle.puzzle_dict
        rows, columns = puzzle_info['rows'], puzzle_info['cols']
        grid_states = puzzle_info['grid_states']
        clues = puzzle_info['clues']
        self.puzzle_frame = PuzzleFrame.from_entry_list(self, rows, columns, grid_states)
        self.puzzle_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.clue_frame = ClueFrame(self, clues)



    def remove_game(self):
        self.puzzle_frame.pack_forget()

    def reset_game(self):
        """Clear everything from all cells, both in the puzzle frame and the clue frame"""
        for entry in self.puzzle_frame.boxes:
            entry.delete(0, tk.END)
            print(entry['state'])



if __name__ == '__main__':
    p = MainWindow()
    p.mainloop()