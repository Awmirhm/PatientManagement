from ttkbootstrap import Window


class Page(Window):
    def __init__(self, weight=1500, height=900):
        super().__init__(themename="superhero")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.geometry(f"{weight}x{height}")
        self.minsize(width=800, height=500)
        self.title("Patient Management")

    def show(self):
        self.mainloop()
