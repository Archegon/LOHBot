from tkinter import *
from tkinter import ttk
from modules import Module
from routines.routines_setup import module_manager


root = Tk()
notebook = ttk.Notebook(root)
root.title("Lord Of Heros Bot")
root.geometry("800x600")
root.minsize(500, 350)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

tab1 = ttk.Frame(notebook)
tab1.columnconfigure(0, weight=7)
tab1.columnconfigure(1, weight=1)
tab1.rowconfigure(0, weight=1)

tab2 = ttk.Frame(notebook)
notebook.add(tab1, text="Modules")
notebook.add(tab2, text="Settings")
notebook.pack(expand=1, fill="both")

module_status = ttk.Frame(tab1, borderwidth=1, relief='solid')
module_status.grid(column=0, row=0, sticky=NSEW)
module_status.rowconfigure(0, weight=1)
module_status.columnconfigure(0, weight=4)
module_status.columnconfigure(1, weight=3)
module_status.columnconfigure(2, weight=1)

module_name_f = ttk.Frame(module_status, borderwidth=1, relief='solid')
module_name_f.grid(column=0, row=0, sticky=NSEW)
module_name_f.columnconfigure(0, weight=1)

module_time_f = ttk.Frame(module_status, borderwidth=1, relief='solid')
module_time_f.grid(column=1, row=0, sticky=NSEW)
module_time_f.columnconfigure(0, weight=1)

module_enable_f = ttk.Frame(module_status, borderwidth=1, relief='solid')
module_enable_f.grid(column=2, row=0, sticky=NSEW)
module_enable_f.columnconfigure(0, weight=1)

module_info = {}
modules = []

for key in Module.instances:
    modules.append(Module.instances[key])


for index, module in enumerate(modules):
    second, minute, hour = module.get_time()
    time_str = f'{hour}H: {minute}M: {second}S'

    temp_dict = {
        index: {
            'name': tk.StringVar(value=module.name),
            'time': tk.StringVar(value=time_str),
            'enable': tk.BooleanVar(value=0)
        }
    }

    module_info.update(temp_dict)

    temp_dict = {
        index: {
            'name_label': ttk.Label(module_name_f, textvariable=module_info[index]['name']),
            'time_label': ttk.Label(module_time_f, textvariable=module_info[index]['time']),
            'enable_box': ttk.Checkbutton(module_enable_f, variable=module_info[index]['enable'])
        }
    }

    module_info.update(temp_dict)

    module_info[index]['name_label'].grid(column=0, row=index, sticky=W)
    module_info[index]['time_label'].grid(column=0, row=index, sticky=W)
    module_info[index]['enable_box'].grid(column=0, row=index, sticky=NSEW)
    module_name_f.rowconfigure(index, weight=1)
    module_time_f.rowconfigure(index, weight=1)
    module_enable_f.rowconfigure(index, weight=1)

module_controls = ttk.Frame(tab1)
module_controls.grid(column=1, row=0, sticky=NSEW)
module_controls.columnconfigure(0, weight=1)
module_controls.rowconfigure(0, weight=1)
module_controls.rowconfigure(1, weight=1)
module_controls.rowconfigure(2, weight=1)

mc_b1 = ttk.Button(module_controls, text="Start")
mc_b1.grid(column=0, row=0, ipady=10, ipadx=10, sticky=S, pady=10)

mc_b2 = ttk.Button(module_controls, text="Stop")
mc_b2.grid(column=0, row=1, ipady=10, ipadx=10, sticky=N, pady=10)

root.mainloop()
