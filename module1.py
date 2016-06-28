import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import tkinter as tk

LARGE_FONT=("Verdana", 12)
class Game (tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column = 0, sticky="nsew")
        self.show_frame(StartPage)
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="START", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text = "TEST Page One",
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="WWW", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text = "TEST Start Page",
                            command=lambda: controller.show_frame(StartPage))
        button.pack()
        f= Figure(figsize=(5,5), dpi=100)
        a=f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)
        toolbar = NavigationToolbar2TkAgg(canvas,self)
        toolbar.updatge()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand = True)
        
        
app = Game()
app.mainloop()
