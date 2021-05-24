from tkinter import *
from tkinter import ttk

root = Tk()
notebook = ttk.Notebook(root)
root.title("Lord Of Heros Bot")
root.geometry("800x600")
root.minsize(500, 350)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

tab1 = ttk.Frame(notebook)
tab1.columnconfigure(0, weight=3)
tab1.columnconfigure(1, weight=1)
tab1.rowconfigure(0, weight=1)

tab2 = ttk.Frame(notebook)
notebook.add(tab1, text="Modules")
notebook.add(tab2, text="Settings")
notebook.pack(expand=1, fill="both")

module_status = ttk.Frame(tab1, borderwidth=1, relief='solid')
module_status.grid(column=0, row=0, sticky=NSEW)

module_controls = ttk.Frame(tab1)
module_controls.grid(column=1, row=0, sticky=NSEW)
module_controls.columnconfigure(0, weight=1)
module_controls.rowconfigure(0, weight=1)
module_controls.rowconfigure(1, weight=1)
module_controls.rowconfigure(2, weight=1)

ms_name1 = ttk.Label(module_status, text="Test")
ms_name1.grid(column=0, row=0, sticky=W)

mc_b1 = ttk.Button(module_controls, text="Start")
mc_b1.grid(column=0, row=0, ipady=10, ipadx=10, sticky=S, pady=10)

mc_b2 = ttk.Button(module_controls, text="Stop")
mc_b2.grid(column=0, row=1, ipady=10, ipadx=10, sticky=N, pady=10)


root.mainloop()
