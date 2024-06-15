from pathlib import Path
import random
from tkinter import Frame, Tk, Canvas,  Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class App(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.geometry("1165x590")
        self.resizable(False, False)

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, minsize=590, weight=1)
        container.grid_columnconfigure(0, minsize=1165, weight=1)
        container.grid_columnconfigure(1, weight=1)

        self.frames = {}


        for F in (GameScreen, StartGame):
            name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.switch_frame("StartGame")

    def switch_frame(self, page_name):
        new_frame = self.frames[page_name]
        new_frame.tkraise()


class GameScreen(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.winText = "Your turn"
        self.computerText = ""
        self.userScore = 0 
        self.computerScore = 0
        self.canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 590,
            width = 1165,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            68.0,
            590.0,
            fill="#3D3D3D",
            outline="")

        self.canvas.create_rectangle(
            1098.0,
            0.0,
            1165.0,
            590.0,
            fill="#3D3D3D",
            outline="")

        self.canvas.create_rectangle(
            68.0,
            0.0,
            1098.0,
            84.0,
            fill="#2B4589",
            outline="")

        self.canvas.create_text(
            83.0,
            26.0,
            anchor="nw",
            text="Score:",
            tags="scorebla",
            fill="#FFFFFF",
            font=("Inter Bold", 21 * -1)
        )

        self.canvas.create_text(
            883.0,
            26.0,
            anchor="nw",
            text="Computer: ",
            tags="computerbla",
            fill="#FFFFFF",
            font=("Inter Bold", 21 * -1)
        )

        self.canvas.create_text(
            1031.0,
            26.0,
            anchor="nw",
            text=self.computerScore,
            tags="computerScore",
            fill="#FFFFFF",
            font=("Inter", 21 * -1)
        )

        self.canvas.create_text(
            197.0,
            26.0,
            anchor="nw",
            text=self.userScore,
            tags="userScore",
            fill="#FFFFFF",
            font=("Inter", 21 * -1)
        )

        self.canvas.create_text(
            410.0,
            146.0,
            anchor="nw",
            text=self.computerText,
            tags="computerText",
            fill="#000000",
            font=("Inter", 26 * -1)
        )

        rock_image = PhotoImage(
            file=relative_to_assets("rock.png"))
        rock_button = Button(
            self.canvas,
            image=rock_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.play('rock'),
            relief="flat"
        )
        rock_button.place(
            x=329.0,
            y=377.0,
            width=90.18537902832031,
            height=90.87959289550781
        )

        paper_image = PhotoImage(
            file=relative_to_assets("paper.png"))
        paper_button = Button(
            self.canvas,
            image=paper_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.play('paper'),
            relief="flat"
        )
        paper_button.place(
            x=531.0,
            y=377.0,
            width=90.18537902832031,
            height=90.87959289550781
        )

        scissor_image = PhotoImage(
            file=relative_to_assets("scissors.png"))
        scissor_button = Button(
            self.canvas,
            image=scissor_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.play('scissors'),
            relief="flat"
        )
        scissor_button.place(
            x=747.0,
            y=377.0,
            width=90.18537902832031,
            height=90.87959289550781
        )
        back_image = PhotoImage(
            file=relative_to_assets("back.png"))
        back_button = Button(
            self.canvas,
            image=back_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.switch_frame("StartGame"),
            relief="flat"
        )
        back_button.place(
            x=442.0,
            y=507.0,
            width=268.0,
            height=52.0
        )

        self.canvas.create_text(
            520.0,
            254.0,
            anchor="nw",
            text=self.winText,
            tags="winText",
            fill="#5A5050",
            font=("Inter SemiBold", 26 * -1)
        )

        rock_button.photo = rock_image
        paper_button.photo = paper_image
        scissor_button.photo = scissor_image
        back_button.photo = back_image

    def show_computer_choice(self):
        self.canvas.delete("computerText")
        self.canvas.create_text(
            410.0,
            146.0,
            anchor="nw",
            text=self.computerText,
            tags="computerText",
            fill="#000000",
            font=("Inter", 26 * -1)
        )
    def show_winner(self):
        self.canvas.delete("winText")
        self.canvas.create_text(
            520.0,
            254.0,
            anchor="nw",
            text=self.winText,
            tags="winText",
            fill="#5A5050",
            font=("Inter SemiBold", 26 * -1)
        )

    def show_score(self):
        self.canvas.delete("userScore")
        self.canvas.create_text(
            197.0,
            26.0,
            anchor="nw",
            text=self.userScore,
            tags="userScore",
            fill="#FFFFFF",
            font=("Inter", 21 * -1)
        )
        self.canvas.delete("computerScore")
        self.canvas.create_text(
            1031.0,
            26.0,
            anchor="nw",
            text=self.computerScore,
            tags="computerScore",
            fill="#FFFFFF",
            font=("Inter", 21 * -1)
        )
    def determine_winner(self, user_choice, computer_choice):
        self.computerText = "Computer Chose: "+ computer_choice
        self.show_computer_choice()
        if user_choice == computer_choice:
            self.winText = 'TIE'
        elif user_choice == 'rock' and computer_choice == 'scissors':
            self.userScore += 1
            self.winText = 'You win'
        elif user_choice == 'paper' and computer_choice == 'rock':
            self.userScore+= 1
            self.winText = 'You win'
        elif user_choice == 'scissors' and computer_choice == 'paper':
            self.userScore+= 1
            self.winText = 'You win'
        else:
            self.computerScore += 1
            self.winText = 'Computer wins'
        self.show_winner()
        self.show_score()

    def play(self, choice):
        self.determine_winner(choice, random.choice(('rock', 'paper', 'scissors')))


class StartGame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 590,
            width = 1165,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            583.0,
            337.0,
            image=image_image_1
        )

        canvas.create_rectangle(
            68.0,
            0.0,
            1098.0,
            84.0,
            fill="#2B4589",
            outline="")

        button_image_1 = PhotoImage(
            file=relative_to_assets("start.png"))
        start_button = Button(
            canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.switch_frame("GameScreen"),
            relief="flat"
        )
        start_button.place(
            x=481.0,
            y=256.0,
            width=204.0,
            height=78.0
        )

        canvas.create_text(
            889.0,
            527.0,
            anchor="nw",
            tags="creator",
            text="Created by \nSargurunathan",
            fill="#0A001D",
            font=("Inter Bold", 21 * -1)
        )

        canvas.create_rectangle(
            1098.0,
            0.0,
            1165.0,
            590.0,
            fill="#3D3D3D",
            outline="")

        canvas.create_rectangle(
            1.0,
            0.0,
            68.0,
            590.0,
            fill="#3D3D3D",
            outline="")

        start_button.photo = button_image_1
        canvas.photo = image_image_1

app = App()
app.mainloop()
