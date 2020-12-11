import tkinter as tk


class GridEntry(tk.Entry):
    def __init__(self, master, grid_num, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.grid_num = grid_num