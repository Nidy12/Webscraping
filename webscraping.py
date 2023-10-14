import tkinter as tk
import pandas as pd
from tkinter.filedialog import askopenfilename
from tkintertable import TableCanvas
# import new2

def import_csv_data():
    global v, df
    csv_file_path = askopenfilename()
    print(csv_file_path)
    v.set(csv_file_path)
    df = pd.read_csv(csv_file_path)

def display_csv_data():
    global df
    if df is not None:
        top = tk.Toplevel()
        table = TableCanvas(top, data= df.T)
        table.show()

root = tk.Tk()
tk.Label(root, text='File Path').grid(row=1, column=0)
v = tk.StringVar()
entry = tk.Entry(root, textvariable=v).grid(row=1, column=1)
# tk.Label(root, text='Enter the pages u want to extract').grid(row=0, column=0)
# limit = tk.Text(root, height=1, width=5).grid(row=0, column=1)
# tk.Button(root, text='Extract', command=new2).grid(row=3, column=0)
# limit.insert(tk.END, "This is some text.")
# limit.pack()
tk.Button(root, text='Browse Data Set', command=import_csv_data).grid(row=2, column=0)
tk.Button(root, text='Display Data Set', command=display_csv_data).grid(row=2, column=1)
tk.Button(root, text='Close', command=root.destroy).grid(row=2, column=2)

df = None
root.mainloop()