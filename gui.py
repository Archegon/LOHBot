import tkinter as tk
import tkinter.ttk as ttk
from routines.routines_setup import module_manager

root = tk.Tk()
notebook = ttk.Notebook(root)
root.title("Lord Of Heros Bot")
root.geometry("800x600")
root.minsize(500, 350)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

module_status = ttk.Frame(tab1, borderwidth=1, relief='solid')
module_status.grid(column=0, row=0, sticky=tk.NSEW)
module_status.rowconfigure(0, weight=1)
module_status.columnconfigure(0, weight=4)
module_status.columnconfigure(1, weight=3)
module_status.columnconfigure(2, weight=1)

module_name_f = ttk.Frame(module_status, borderwidth=1, relief='solid')
module_name_f.grid(column=0, row=0, sticky=tk.NSEW)
module_name_f.columnconfigure(0, weight=1)

module_time_f = ttk.Frame(module_status, borderwidth=1, relief='solid')
module_time_f.grid(column=1, row=0, sticky=tk.NSEW)
module_time_f.columnconfigure(0, weight=1)

module_enable_f = ttk.Frame(module_status, borderwidth=1, relief='solid')
module_enable_f.grid(column=2, row=0, sticky=tk.NSEW)
module_enable_f.columnconfigure(0, weight=1)

module_info = {}

for index, module in enumerate(module_manager.get_modules()):
    second, minute, hour = module.get_time()
    time_str = f'{hour}H: {minute}M: {second}S'

    temp_dict = {
        index: {
            'name': module.name,
            'time': time_str,
            'enable': tk.IntVar(value=0)
        }
    }

    module_info.update(temp_dict)

    temp_dict = {
        index: {
            'name_label': ttk.Label(module_name_f, text=module_info[index]['name']),
            'time_label': ttk.Label(module_time_f, text=module_info[index]['time']),
            'enable_box': ttk.Checkbutton(module_enable_f, variable=module_info[index]['enable'])
        }
    }

    module_info.update(temp_dict)

    module_info[index]['name_label'].grid(column=0, row=index, sticky=tk.W)
    module_info[index]['time_label'].grid(column=0, row=index, sticky=tk.W)
    module_info[index]['enable_box'].grid(column=0, row=index)
    module_name_f.rowconfigure(index, weight=1)
    module_time_f.rowconfigure(index, weight=1)
    module_enable_f.rowconfigure(index, weight=1)

module_controls = ttk.Frame(tab1)
module_controls.grid(column=1, row=0, sticky=tk.NSEW)
module_controls.columnconfigure(0, weight=1)
module_controls.rowconfigure(0, weight=1)
module_controls.rowconfigure(1, weight=1)
module_controls.rowconfigure(2, weight=1)

mc_b1 = ttk.Button(module_controls, text="Start")
mc_b1.grid(column=0, row=0, ipady=10, ipadx=10, sticky=tk.S, pady=10)

mc_b2 = ttk.Button(module_controls, text="Stop")
mc_b2.grid(column=0, row=1, ipady=10, ipadx=10, sticky=tk.N, pady=10)

root.mainloop()


class NoteBook:
    def __int__(self, master):
        self.master = master
        self.notebook = ttk.Notebook(self.master)
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)

    def setup_tabs(self):
        self.tab1.columnconfigure(0, weight=7)
        self.tab1.columnconfigure(1, weight=1)
        self.tab1.rowconfigure(0, weight=1)

        self.notebook.add(self.tab1, text="Modules")
        self.notebook.add(self.tab2, text="Settings")
        self.notebook.pack(expand=1, fill="both")
