import tkinter as tk

class view(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self.label = tk.Label(self, text="App")
        self.label.pack(pady=5)
        self.button = tk.Button(self, text="Fish", command=self.controller.run)
        self.button.pack(pady=5)

        self.pack()