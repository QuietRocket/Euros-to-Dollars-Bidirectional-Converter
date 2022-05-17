import tkinter as tk

class Converter:
    

    def __init__(self):
        # Creating the window
        root = tk.Tk()
        root.geometry("270x85")
        root.resizable(False, False)
        
        # Initializing variables
        euros = tk.StringVar(root, value=0)
        dollars = tk.StringVar(root, value=0)
        rate = tk.StringVar(root, value=1.05)
        direction = tk.StringVar(root, value="=>")

        # First row
        top_frame = tk.Frame(root)
        top_frame.pack()
        tk.Entry(top_frame, textvariable=euros, width=10).pack(side=tk.LEFT)
        tk.Label(top_frame, text="€").pack(side=tk.LEFT)
        tk.Label(top_frame, textvariable=direction).pack(side=tk.LEFT)
        tk.Entry(top_frame, textvariable=dollars, width=10).pack(side=tk.LEFT)
        tk.Label(top_frame, text="$").pack(side=tk.LEFT)

        # Second row
        bottom_frame = tk.Frame(root)
        bottom_frame.pack()
        tk.Label(bottom_frame, text="TAUX : 1 € =").pack(side=tk.LEFT)
        tk.Spinbox(bottom_frame, textvariable=rate, width=10).pack(side=tk.LEFT)
        tk.Label(bottom_frame, text="$").pack(side=tk.LEFT)

        tk.Button(root, text="Quitter", command=self.quit).pack(fill=tk.BOTH)

        self.__root = root
        self.__euros = euros
        self.__dollars = dollars
        self.__rate = rate
        self.__direction = direction

        root.mainloop()
    
    def toDollars(self, s: float) -> None:
        pass

    def toEuros(self, s: float) -> None:
        pass

    def setTaux(self, s: float) -> None:
        pass

    def quit(self):
        self.root.quit()