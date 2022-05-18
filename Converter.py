import tkinter as tk

class Converter:
    def __init__(self):
        # Creating the window
        root = tk.Tk()
        root.geometry("270x85")
        root.title("Convertisseur")
        root.resizable(False, False)
        
        # Initializing variables
        euros = tk.StringVar(root, value=0)
        dollars = tk.StringVar(root, value=0)
        rate = tk.StringVar(root, value=1.05)
        direction = tk.StringVar(root, value="=>")

        # First row
        top_frame = tk.Frame(root)
        top_frame.pack()
        euros_entry = tk.Entry(top_frame, textvariable=euros, width=10)
        euros_entry.pack(side=tk.LEFT)
        tk.Label(top_frame, text="€").pack(side=tk.LEFT)
        tk.Label(top_frame, textvariable=direction).pack(side=tk.LEFT)
        dollars_entry = tk.Entry(top_frame, textvariable=dollars, width=10)
        dollars_entry.pack(side=tk.LEFT)
        tk.Label(top_frame, text="$").pack(side=tk.LEFT)

        # Second row
        bottom_frame = tk.Frame(root)
        bottom_frame.pack()
        tk.Label(bottom_frame, text="TAUX : 1 € =").pack(side=tk.LEFT)
        rate_spinbox = tk.Spinbox(bottom_frame, textvariable=rate, width=10, from_=0, to=100, increment=0.01)
        rate_spinbox.pack(side=tk.LEFT)
        tk.Label(bottom_frame, text="$").pack(side=tk.LEFT)

        # Event bindings for enter event on entries and spinbox
        rate_spinbox.configure(command=lambda: self.setTaux(self.rate))
        euros_entry.bind("<Return>", lambda event: self.toDollars(self.euros))
        dollars_entry.bind("<Return>", lambda event: self.toEuros(self.dollars))

        tk.Button(root, text="Quitter", command=self.quit).pack(fill=tk.BOTH)

        self.__root = root
        self.__euros = euros
        self.__dollars = dollars
        self.__rate = rate
        self.__direction = direction

        root.mainloop()
    
    @property
    def dollars(self):
        return float(self.__dollars.get())
    
    @dollars.setter
    def dollars(self, value):
        self.__dollars.set(value)
        
    @property
    def euros(self):
        return float(self.__euros.get())
    
    @euros.setter
    def euros(self, value):
        self.__euros.set(value)

    @property
    def rate(self):
        return float(self.__rate.get())
    
    @rate.setter
    def rate(self, value):
        self.__rate.set(value)

    def toDollars(self, s: float) -> None:
        self.__direction.set("=>")
        self.dollars = s * self.rate

    def toEuros(self, s: float) -> None:
        self.__direction.set("<=")
        self.euros = s / self.rate

    def setTaux(self, s: float) -> None:
        self.rate = s

    def quit(self):
        self.__root.quit()