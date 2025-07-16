import tkinter as tk
from controller import controller
from init import fishingModel

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Fishing App")
    root.geometry("200x100")

    app = controller(root, fishingModel)

    root.mainloop()