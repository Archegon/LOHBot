import tkinter as tk
import tkinter.ttk as ttk
from routines.routines_setup import module_manager

root = tk.Tk()
root.title("Lord Of Heros Bot")
root.geometry("800x600")
root.minsize(500, 350)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)


class NoteBook:
    def __init__(self, master):
        self.master = master
        self.notebook = ttk.Notebook(self.master)
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.setup_tabs()

    def setup_tabs(self):
        self.tab1.columnconfigure(0, weight=7)
        self.tab1.columnconfigure(1, weight=1)
        self.tab1.rowconfigure(0, weight=1)
        self.tab_1_setup()

        self.notebook.add(self.tab1, text="Modules")
        self.notebook.add(self.tab2, text="Settings")
        self.notebook.pack(expand=1, fill="both")

    def tab_1_setup(self):
        self.ModuleStatusFrame(self.tab1)
        self.ModuleControlsFrame(self.tab1)

    class ModuleStatusFrame(tk.Frame):
        def __init__(self, master):
            super().__init__(master)
            self["borderwidth"] = 1
            self["relief"] = 'solid'
            self.module_name = ttk.Frame(self, borderwidth=1, relief='solid')
            self.module_time = ttk.Frame(self, borderwidth=1, relief='solid')
            self.module_enable = ttk.Frame(self, borderwidth=1, relief='solid')
            self.setup()

        def setup(self):
            self.grid(column=0, row=0, sticky=tk.NSEW)
            self.rowconfigure(0, weight=1)
            self.columnconfigure(0, weight=4)
            self.columnconfigure(1, weight=3)
            self.columnconfigure(2, weight=1)

            self.module_name.grid(column=0, row=0, sticky=tk.NSEW)
            self.module_name.columnconfigure(0, weight=1)
            self.module_time.grid(column=1, row=0, sticky=tk.NSEW)
            self.module_time.columnconfigure(0, weight=1)
            self.module_enable.grid(column=2, row=0, sticky=tk.NSEW)
            self.module_enable.columnconfigure(0, weight=1)

    class ModuleControlsFrame(tk.Frame):
        def __init__(self, master):
            super().__init__(master)
            self.start_b = ttk.Button(self, text="Start")
            self.stop_b = ttk.Button(self, text="Stop")
            self.setup()

        def setup(self):
            self.grid(column=1, row=0, sticky=tk.NSEW)
            self.columnconfigure(0, weight=1)
            self.rowconfigure(0, weight=1)
            self.rowconfigure(1, weight=1)
            self.rowconfigure(2, weight=1)
            self.start_b.grid(column=0, row=0, ipady=10, ipadx=10, sticky=tk.S, pady=10)
            self.stop_b.grid(column=0, row=1, ipady=10, ipadx=10, sticky=tk.N, pady=10)


notebook = NoteBook(root)
root.mainloop()
