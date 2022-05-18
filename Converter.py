import tkinter as tk
from tkinter import messagebox

class Converter:
    def __init__(self):
        # Creating the window
        root = tk.Tk()
        root.geometry("270x85")
        root.title("Convertisseur")
        root.resizable(False, False)

        # Delegate error handeling
        root.report_callback_exception = self.showError
        
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
        rate_spinbox.bind('<Return>', lambda event: self.setTaux(self.rate))
        euros_entry.bind("<Return>", lambda event: self.toDollars(self.euros))
        dollars_entry.bind("<Return>", lambda event: self.toEuros(self.dollars))

        tk.Button(root, text="Quitter", command=self.quit).pack(fill=tk.BOTH)

        self.__root = root
        self.__euros = euros
        self.__dollars = dollars
        self.__rate = rate
        self.__direction = direction

        root.mainloop()
    
    def showError(self, cls, err, traceback):
        error_name = cls.__name__
        error_message = str(err)

        messagebox.showerror(error_name, f"{error_name}: {error_message}")

    @property
    def dollars(self):
        return float(self.__dollars.get())
    
    @dollars.setter
    def dollars(self, value):
        self.__dollars.set(f"{value:.2f}")
        
    @property
    def euros(self):
        return float(self.__euros.get())
    
    @euros.setter
    def euros(self, value):
        self.__euros.set(f"{value:.2f}")

    @property
    def rate(self):
        return float(self.__rate.get())
    
    @rate.setter
    def rate(self, value):
        self.__rate.set(value)

    @property
    def direction(self):
        # =>, true, euros to dollars
        # <=, false, dollars to euros
        return self.__direction.get() == "=>"
    
    @direction.setter
    def direction(self, value):
        self.__direction.set("=>" if value else "<=")

    def toDollars(self, s: float) -> None:
        self.direction = True
        self.dollars = s * self.rate

    def toEuros(self, s: float) -> None:
        self.direction = False
        self.euros = s / self.rate

    def setTaux(self, s: float) -> None:
        if self.direction: # Euros to dollars
            self.dollars = self.euros * s
        else: # Dollars to euros
            self.euros = self.dollars / s

    def quit(self):
        self.__root.quit()