import tkinter as tk
import tkinter.ttk as ttk
import random

from PuzzleFrame import PuzzleFrame
from ClueFrame import ClueFrame
"""
This class will allow the user to enter a list of questions.
Input fields should be what?
    Clue Text
    Answer Length
    Answer Numbers
    

"""
MIN_GRID_WIDTH, MIN_GRID_HEIGHT = 3, 3
MAX_GRID_WIDTH, MAX_GRID_HEIGHT = 5, 5


class EnterNewPuzzleWindow(tk.Toplevel):
    def __init__(self, master, **kwargs):
        super().__init__(**kwargs)

        self.master = master
        # self.root = tk.Toplevel(self.master)
        self.transient(self.master)
        self._default_x = 1000
        self._default_y = 600

        self.geometry(self._get_spawn_position())

        self.title('Enter Cluuse!')
        self.puzzle_grid_width = tk.IntVar()
        self.puzzle_grid_height = tk.IntVar()
        self.clue = tk.StringVar()
        self.clue_numbers = tk.StringVar()

        # these values are updated in the generate_puzzle method
        self.puzzle_dict = {'rows': 0, 'cols': 0, 'grid_states': [], 'clues': {}}
        self.clue_list = []

        # Define all the frames the input widgets will appear in

        input_frame = tk.Frame(self, bg='darkorange')
        puzzle_dimensions_frame = tk.Frame(input_frame, bg='grey')
        button_frame = tk.Frame(input_frame, bg='purple')
        clue_entry_frame = tk.Frame(input_frame, bg='green')
        puzzle_preview_frame = tk.Frame(self, bg='white', width=500)
        self.grid_preview_frame = tk.Frame(puzzle_preview_frame)
        self.clue_preview_frame = ClueFrame(puzzle_preview_frame, self.clue_list)
        puzzle_preview_frame.propagate(False)
        self.grid_preview = None

         # Label widgets
        puzzle_width_label = tk.Label(puzzle_dimensions_frame, text='Puzzle Grid Width')
        puzzle_height_label = tk.Label(puzzle_dimensions_frame, text='Puzzle Grid Height')
        clue_label = tk.Label(clue_entry_frame, text='Clue: ')
        clue_length_numbers_label = tk.Label(clue_entry_frame, text='Numbers for each answer')

        # Input widgets
        puzzle_width_spinbox = tk.Spinbox(puzzle_dimensions_frame, from_=MIN_GRID_WIDTH, to=MAX_GRID_WIDTH, textvar=self.puzzle_grid_width)
        puzzle_height_spinbox = tk.Spinbox(puzzle_dimensions_frame, from_=MIN_GRID_HEIGHT, to=MAX_GRID_HEIGHT, textvar=self.puzzle_grid_height)

        puzzle_width_spinbox.bind('<Button-4>', self.increase_spinbox)
        puzzle_width_spinbox.bind('<Button-5>', self.decrease_spinbox)
        puzzle_height_spinbox.bind('<Button-4>', self.increase_spinbox)
        puzzle_height_spinbox.bind('<Button-5>', self.decrease_spinbox)

        clue_entry = tk.Entry(clue_entry_frame, textvar=self.clue)
        clue_numbers_entry = tk.Entry(clue_entry_frame, textvar=self.clue_numbers)

        # Buttons what do stuff
        self.add_clue_button = tk.Button(button_frame, text='Add Clue', command=self.add_clue)
        self.finish_button = tk.Button(button_frame, text='Generate Puzzle', command=self.generate_puzzle)
        self.cancel_button = tk.Button(button_frame, text='Cancel', command=self.on_cancel)
        mini_puzzle_grid_button = tk.Button(puzzle_dimensions_frame, text='Generate Grid Preview', command=self.generate_grid_preview)
        mini_clues_button = tk.Button(clue_entry_frame, text='Add Clue', command=self.add_clue)

        # Placing the widgets into their frames using grid or pack #
        puzzle_width_label.grid(row=1, column=1)
        puzzle_height_label.grid(row=2, column=1)
        puzzle_width_spinbox.grid(row=1, column=2)
        puzzle_height_spinbox.grid(row=2, column=2)
        mini_puzzle_grid_button.grid(row=3, column=1)
        mini_clues_button.grid(row=3, column=0, sticky='w')

        clue_label.grid(row=1, column=0, sticky='w')
        clue_entry.grid(row=1, column=1, sticky='w', padx=5)
        clue_length_numbers_label.grid(row=2, column=0, sticky='w')
        clue_numbers_entry.grid(row=2, column=1, sticky='w', padx=5)

        self.add_clue_button.pack(side=tk.LEFT, padx=(20, 0))
        self.finish_button.pack(side=tk.LEFT, padx=(10, 10))
        self.cancel_button.pack(side=tk.LEFT, padx=(0, 30))

        # Packing the frames into the master window
        puzzle_preview_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        self.grid_preview_frame.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        self.clue_preview_frame.pack(side=tk.BOTTOM, expand=False, fill=tk.X)
        input_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        puzzle_dimensions_frame.grid(row=0, column=0, sticky='w', pady=(5, 10))
        clue_entry_frame.grid(row=1, column=0, sticky='w', pady=(50, 10))
        # button_frame.pack(side=tk.BOTTOM, expand=True, fill=tk.X)
        button_frame.grid(row=2, column=0, sticky='ew', pady=30)

    def _calculate_window_position(self):
        """Calculate the middle of the master widget window position. That location is where this widget will spawn"""
        master_widget_width = self.master.winfo_width()
        master_widget_height = self.master.winfo_height()
        middle_x = str(int(master_widget_width / 2))
        middle_y = str(int(master_widget_height / 2))

        return f'+{middle_x}+{middle_y}'

    def _get_next_clue_num(self):
        # next_num = self._clue_num + 1
        # self._clue_num += 1
        # return next_num

        # not sure if doing this is better than what is done above, but it seems more elegant doing it this way
        # further, according to https://wiki.python.org/moin/TimeComplexity,
        # the len() function time to return is invariant with its argument length

        next_num = len(self.clue_list) + 1
        return next_num

    def _get_spawn_position(self):
        x_y_offset = self._calculate_window_position()
        spawn_position = f'{self._default_x}x{self._default_y}'
        spawn_position += x_y_offset

        return spawn_position

    def add_clue(self):
        """Add a clue to the clue_dict variable
        It will be formatted thusly: {int: (str, []), ...}
        After the clue is entered the entry field will be cleared"""

        clue = self.clue.get()
        if clue:
            # clue_length = self.clue_length.get()
            clue_num_list = self.clue_numbers.get().split(',')
            new_clue = [clue, clue_num_list]
            # new_clue_num = self._get_next_clue_num()
            self.clue_list.append(new_clue)
            self.clear_clue()
            self.clear_clue_preview()
            self.clue_preview_frame.update_clue_layout(new_clue)

    def clear_clue(self):
        """Clear Entry widgets for entering clues"""
        self.clue.set('')
        self.clue_numbers.set('')

    def clear_clue_preview(self):
        for child in self.clue_preview_frame.winfo_children():
            tk.Grid.grid_forget(child)

    def generate_grid_preview(self):
        """Populate the puzzle_preview_frame with a grid which will be the puzzle grid.
        If called again the previous grid will be discarded"""
        for child in self.grid_preview_frame.winfo_children():
            child.pack_forget()

        rows = self.puzzle_grid_height.get()
        columns = self.puzzle_grid_width.get()
        self.grid_preview = PuzzleFrame(self.grid_preview_frame, rows=rows, columns=columns)

    def generate_puzzle(self):
        """Assign values to the puzzle_dict variable.
        Namely: puzzle_dict['rows'], puzzle_dict['cols'], puzzle_dict['grid_states'], and puzzle_dict['clues']
        Puzzle_dict will be accessed by the PuzzleFrame of the main window to make the final grid"""
        self.puzzle_dict['rows'] = self.puzzle_grid_height.get()
        self.puzzle_dict['cols'] = self.puzzle_grid_width.get()
        self.puzzle_dict['grid_states'] = [child['state'] for child in self.grid_preview.winfo_children()]
        self.puzzle_dict['clue_list'] = self.clue_list
        self.destroy()

    def increase_spinbox(self, event=None):
        sb = event.widget
        next_num = int(sb.get()) + 1
        if next_num > sb['to']:
            next_num = int(sb['from'])

        sb.delete(0, tk.END)
        sb.insert(1, next_num)
        return 'break'

    def decrease_spinbox(self, event=None):
        sb = event.widget
        next_num = int(sb.get()) + 1
        if next_num < sb['from']:
            next_num = int(sb['to'])

        sb.delete(0, tk.END)
        sb.insert(1, next_num)
        return 'break'

    def on_cancel(self):
        """Close this window without doing anything"""
        if __name__ == '__main__':
            self.master.destroy()
        else:
            self.puzzle_dict = None
            self.destroy()





if __name__ == "__main__":
    mw = tk.Tk()
    mw.title('IDK')
    mw.geometry('100x100+1500+0')
    fw = EnterNewPuzzleWindow(mw)
    mw.mainloop()
