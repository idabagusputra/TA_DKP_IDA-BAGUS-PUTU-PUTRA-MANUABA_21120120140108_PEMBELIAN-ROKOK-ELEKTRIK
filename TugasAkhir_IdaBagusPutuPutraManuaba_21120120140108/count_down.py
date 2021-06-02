import tkinter as tk

class HM(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("PAKET TERSEDIA DALAM")
        self.iconbitmap("C:/GUI/vape1.ico")
        self.label = tk.Label(self, text="", width="300",height="90", font=("Calibri", 13))
        self.label.pack()
        self.geometry("350x100")
        self.remaining = 0
        self.countdown(3)

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.label.configure(text="PAKET ANDA TELAH TERSEDIA", bg="gray", width="300", height="90", font=("Calibri", 13))

        else:
            self.label.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)