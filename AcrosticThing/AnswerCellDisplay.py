import tkinter as tk


# TODO: when the last answer cell is active and Tab or a key is released, focus traversal moves
# to the parent object. The PuzzleFrame or ClueDisplay (generally the AnswerCellDisplay) and
# throws an error. fix that
class AnswerCellDisplay(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.answer_cells = []
        self.generate_answer_cells()
        self.bind_events()
        # self.pack()

    def allow_focus_traversal(self, event=None):
        self.configure(takefocus=1)
        for cell in self.answer_cells:
            cell.configure(takefocus=1)

    def bind_events(self):
        # self.deny_focus_traversal()
        # self.bind('<Enter>', self.allow_focus_traversal)
        # self.bind('<Leave>', self.deny_focus_traversal)

        for cell in self.answer_cells:
            cell.set_binding('<Enter>', 'toggle_highlight')
            cell.set_binding('<Leave>', 'toggle_highlight')
            cell.bind('<KeyRelease>', self.focus_next_entry)

    def deny_focus_traversal(self, event=None):
        self.configure(takefocus=0)
        for cell in self.answer_cells:
            cell.configure(takefocus=0)

    def focus_next_entry(self, event=None):
        passable_events = ['Tab', 'BackSpace', 'Delete', 'Shift_L', 'Shift_R']
        if event.keysym in passable_events:
            pass
        else:
            curr_cell = event.widget
            next_cell = curr_cell.tk_focusNext()
            next_cell.focus()
            next_cell.selection_range(0, tk.END)

    def generate_answer_cells(self):
        """To be implemented by inherited classes"""
        pass

    def reset_cells(self):
        for cell in self.answer_cells:
            cell.delete(0, tk.END)