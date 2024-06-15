from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/sarguru/dev/Projects/encryptix/calculator/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class Calculator():
    def __init__(self):
        self.exp = ""
        window = Tk()

        window.geometry("411x823")
        window.configure(bg = "#212020")


        self.canvas = Canvas(
            window,
            bg = "#212020",
            height = 823,
            width = 411,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            291.0,
            411.0,
            823.0,
            fill="#F0F0F3",
            outline="")

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handleNum(1),
            relief="flat"
        )
        button_1.place(
            x=38.0,
            y=631.8974609375,
            width=72.0,
            height=70.1025390625
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handleNum(2),
            relief="flat"
        )
        button_2.place(
            x=128.0,
            y=631.8974609375,
            width=71.0,
            height=70.1025390625
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handleNum(3),
            relief="flat"
        )
        button_3.place(
            x=218.0,
            y=631.8974609375,
            width=71.0,
            height=70.1025390625
        )

        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_plus = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handleOp("+"),
            relief="flat"
        )
        button_plus.place(
            x=308.0,
            y=631.8974609375,
            width=71.0,
            height=70.1025390625
        )

        button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        button_4 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:self.handleNum(4),
            relief="flat"
        )
        button_4.place(
            x=38.0,
            y=537.8974609375,
            width=72.0,
            height=70.1025390625
        )

        button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        button_5 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handleNum(5),
            relief="flat"
        )
        button_5.place(
            x=128.0,
            y=537.8974609375,
            width=71.0,
            height=70.1025390625
        )

        button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        button_6 = Button(
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handleNum(6),
            relief="flat"
        )
        button_6.place(
            x=218.0,
            y=537.8974609375,
            width=71.0,
            height=70.1025390625
        )

        button_image_8 = PhotoImage(
            file=relative_to_assets("button_8.png"))
        button_sub = Button(
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handleOp("-"),
            relief="flat"
        )
        button_sub.place(
            x=308.0,
            y=537.8974609375,
            width=71.0,
            height=70.1025390625
        )

        button_image_9 = PhotoImage(
            file=relative_to_assets("button_9.png"))
        button_7 = Button(
            image=button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handleNum(7),
            relief="flat"
        )
        button_7.place(
            x=38.0,
            y=443.8974304199219,
            width=72.0,
            height=70.10256958007812
        )

        button_image_10 = PhotoImage(
            file=relative_to_assets("button_10.png"))
        button_8 = Button(
            image=button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handleNum(8),
            relief="flat"
        )
        button_8.place(
            x=128.0,
            y=443.8974304199219,
            width=71.0,
            height=70.10256958007812
        )

        button_image_11 = PhotoImage(
            file=relative_to_assets("button_11.png"))
        button_9 = Button(
            image=button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handleNum(9),
            relief="flat"
        )
        button_9.place(
            x=218.0,
            y=443.8974304199219,
            width=71.0,
            height=70.10256958007812
        )

        button_image_12 = PhotoImage(
            file=relative_to_assets("button_12.png"))
        button_mul = Button(
            image=button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handleOp("*"),
            relief="flat"
        )
        button_mul.place(
            x=308.0,
            y=443.8974304199219,
            width=71.0,
            height=70.10256958007812
        )

        button_image_13 = PhotoImage(
            file=relative_to_assets("button_13.png"))
        button_clear = Button(
            image=button_image_13,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handleClear(),
            relief="flat"
        )
        button_clear.place(
            x=38.0,
            y=349.8974304199219,
            width=72.0,
            height=70.10256958007812
        )

        button_image_14 = PhotoImage(
            file=relative_to_assets("button_14.png"))
        button_div = Button(
            image=button_image_14,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handleOp("/"),
            relief="flat"
        )
        button_div.place(
            x=308.0,
            y=349.8974304199219,
            width=71.0,
            height=70.10256958007812
        )

        button_image_15 = PhotoImage(
            file=relative_to_assets("button_15.png"))
        button_mod = Button(
            image=button_image_15,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handleOp("%"),
            relief="flat"
        )
        button_mod.place(
            x=218.0,
            y=349.8974304199219,
            width=71.0,
            height=70.10256958007812
        )

        button_image_16 = PhotoImage(
            file=relative_to_assets("button_16.png"))
        button_clearAll = Button(
            image=button_image_16,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handleClearAll(),
            relief="flat"
        )
        button_clearAll.place(
            x=128.0,
            y=349.8974304199219,
            width=71.0,
            height=70.10256958007812
        )

        button_image_17 = PhotoImage(
            file=relative_to_assets("button_17.png"))
        button_0 = Button(
            image=button_image_17,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handleNum(0),
            relief="flat"
        )
        button_0.place(
            x=39.0,
            y=725.8974609375,
            width=250.0,
            height=70.1025390625
        )

        button_image_18 = PhotoImage(
            file=relative_to_assets("button_18.png"))
        button_res = Button(
            image=button_image_18,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handleResult(),
            relief="flat"
        )
        button_res.place(
            x=308.0,
            y=725.8974609375,
            width=71.0,
            height=70.1025390625
        )
        self.showTextOnCanvas()
        window.resizable(False, False)
        window.mainloop()


    def handleOp(self, op):
        self.exp += op
        self.showTextOnCanvas()

    def handleNum(self, num):
        self.exp += str(num)
        self.showTextOnCanvas();

    def handleClear(self):
        self.exp = self.exp[:-1]
        self.showTextOnCanvas()

    def handleClearAll(self):
        self.exp = ""
        self.showTextOnCanvas()

    def handleResult(self):
        try:
            self.exp = str(eval(self.exp))
        except: 
            self.exp = "Infinity" 
        finally:
            self.showTextOnCanvas()


    def showTextOnCanvas(self):
        self.canvas.delete("exp")
        self.canvas.create_text(
            248.54446411132812,
            195.0,
            anchor="nw",
            text=self.exp,
            tags="exp",
            fill="#F2F2F4",
            font=("Oswald Medium", 64 * -1)
        )

if __name__ == "__main__":
    Calculator()

