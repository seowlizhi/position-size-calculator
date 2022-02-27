import tkinter as tk

# fixed variable
risk_value = 1/100



class Calculator():
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("400x400")

        # Balance part
        self.balance_label = tk.Label(self.window, text= 'Balance: ').pack()
        self.balance = tk.Entry(self.window)
        self.balance.pack()


        # Entry part
        self.entry_label = tk.Label(self.window, text= 'Entry: ').pack()
        self.entry = tk.Entry(self.window)
        self.entry.pack()


        # Stop loss part
        self.sl_label = tk.Label(self.window, text= 'Stop Loss: ').pack()
        self.sl = tk.Entry(self.window)
        self.sl.pack()


        # Take profit part
        self.tp_label = tk.Label(self.window, text= 'Take Profit: ').pack()
        self.tp = tk.Entry(self.window)
        self.tp.pack()


        # Calculate button
        self.submit = tk.Button(self.window, text= "Calculate! ", command = self.calculate)
        self.submit.pack()


        # purchase size
        self.size_label = tk.Label(self.window, text= 'Size: ')
        self.size_label.pack()


        # RR ratio
        self.rr_ratio = tk.Label(self.window, text= 'RR Ratio: ')
        self.rr_ratio.pack()
    

    def ratio(self):
        true_sl = abs(float(self.entry.get())- float(self.sl.get()))
        true_tp = abs(float(self.entry.get()) - float(self.tp.get()))

        self.r = (true_sl/true_sl and true_tp/true_sl)

        self.rr_ratio["text"] = 'RR Ratio: ' + str(self.r)


    def calculate(self):
        if(self.entry.get() != "" and self.sl.get() != ""):
            # get position differents
            a = float(self.entry.get())
            b = float(self.sl.get())
            pos_dif = a-b

            # get size
            self.size = abs(risk_value *  self.balance.get()/ pos_dif)

            self.size_label["text"] = 'Size: ' + str(self.size)

        if(self.entry.get() != "" and self.sl.get() != "" and self.tp.get() != ""):
            self.ratio()
        


if __name__ == "__main__" :
    calculator = Calculator()
    tk.mainloop()
