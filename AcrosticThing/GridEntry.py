import tkinter as tk


class GridEntry(tk.Entry):
    def __init__(self, master, grid_num=0, colors=None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.grid_num = grid_num
        self.colors = colors
        try:
            self.configure(bg=self.colors['bg'], fg=self.colors['fg'])
        except KeyError as e:
            print(e)
        except TypeError as e:
            print(e)

        h = self.register(self.validate_entry)
        self.configure(validate='key', validatecommand=(h, '%d', '%S', '%i', '%P'))

    def clear_bindings(self):
        self.unbind_all('<Enter>')
        self.unbind_all('<Leave>')

    def toggle_highlight(self, event=None):
        if self['bg'] == self.colors['highlight']:
            self.configure(bg=self.colors['unhighlight'])
        else:
            self.configure(bg=self.colors['highlight'])

    def set_binding(self, event, func):
        if func == 'toggle_highlight':
            self.bind(event, self.toggle_highlight)
        if func == 'toggle_state':
            self.bind(event, self.toggle_state)

    def toggle_state(self, event=None):
        if self['state'] == 'normal':
            self.configure(state='disabled', disabledbackground='black')
        else:
            self.configure(state='normal')
        return 'break'

    def validate_entry(self, action, inserted, index, new):
        if action == '0':
            return True
        elif action == '1':
            if index == '0':
                self.delete(0, tk.END)
                self.insert(0, inserted)

                # reset the validate option as it is set to none after delete is called
                self.after_idle(lambda: self.configure(validate='key'))
                return True
        return False


if __name__ == '__main__':
    win = tk.Tk()
    colors = {'fg': 'black', 'bg': 'white'}
    frame = tk.Frame(win)
    first = GridEntry(frame, colors=colors)
    second = tk.Entry(frame)
    first.pack()
    second.pack()
    frame.pack()
    win.mainloop()