# Отрефакторить программу с прошлой домашней работы
# ИЛИ калькулятор с практической работы на ООП стиль.

import tkinter as tk





class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.operation=""
        for i in range(1,4):
            for j in range(3):
                value=(i-1)*3+j+1
                self.button=tk.Button(self,text=f"{value}",width=5,height=5,background="gray",fg="red",font=("Arial Bold",20),command=lambda x=value:self.press(x))
                self.button.grid(row=i,column=j)
        self.plus_button = tk.Button(self, text="+", width=5, height=3, background="gray", foreground="red",
                                font=("Arial Bold", 20), command=lambda x="+": self.press(x))
        self.plus_button.grid(row=1, column=3)
        self.mult_button = tk.Button(self, text="*", width=5, height=3, background="gray", foreground="red",
                                font=("Arial Bold", 20), command=lambda x="*": self.press(x))
        self.mult_button.grid(row=2, column=3)
        self.min_button = tk.Button(self, text="-", width=5, height=3, background="gray", foreground="red",
                               font=("Arial Bold", 20), command=lambda x="-": self.press(x))
        self.min_button.grid(row=3, column=3)
        self.div_button = tk.Button(self, text="/", width=5, height=3, background="gray", foreground="red",
                               font=("Arial Bold", 20), command=lambda x="/": self.press(x))
        self.div_button.grid(row=4, column=3)
        self.eq_button = tk.Button(self, text="=", width=5, height=3, background="gray", foreground="red",
                              font=("Arial Bold", 20), command=lambda x=self.operation: self.eq(x))
        self.eq_button.grid(row=0, column=3)
        self.zero_button = tk.Button(self, text="0", width=5, height=3, background="gray", foreground="red",
                                font=("Arial Bold", 20), command=lambda x="0": self.press(x))
        self.zero_button.grid(row=4, column=0, columnspan=3, sticky="EW")

        self.label = tk.Label(
            self,
            text="",
            fg="black",
            bg="white",
            font=("Arial Bold", 10),
            width=5,
            height=5)
        self.label.grid(row=0, column=0, columnspan=3, sticky="EW")

    def press(self,num):
        self.operation+=str(num)
        self.label["text"]=self.operation
        print(num)

    def eq(self,val):
        answer=eval(val)
        self.label["text"]+="="
        self.label["text"]+=str(answer)



calc=Calculator()
calc.mainloop()