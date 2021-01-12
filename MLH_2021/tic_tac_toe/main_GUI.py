# MAIN GUI FOR TIC TAC TOE GAME
# Santiago Garcia Arango
# MLH2021

# My own imports
import tic_tac_toe as ttt

# General imports
import os
import tkinter as tk
from PIL import Image, ImageTk

# Some constants for the implementation of the code...
current_folder = os.path.dirname(__file__)  # Current working directory

# Remark: When we inherit "tk.Canvas", we obtain the mehods of the default...
# ...Canvas class [canvas = tk.Canvas() ] in our TicTacToeGUI class
class TicTacToeGUI(tk.Canvas):
    def __init__(self):
        # We pass some properties to Canvas from the inheritance properties
        super().__init__(width=700, height=700, background="black", highlightthickness=0)

        # Start main tic tac toe game
        self.game = ttt.TicTacToe()

        # Initialie and restart all important GUI-related things
        self.GUI_initialize()

    def GUI_initialize(self):
        # We call the methods for the canvas GUI creation
        self.load_images()
        self.create_objects()

        # We bind the functionalities of the keyboard presses
        # bind_all:"<Key>" let us react to event of keypress...
        # self.on_key_press: is called after the event of a keypress
        self.bind_all("<Key>", self.on_key_press)

        # We bind the functionalities of the mouse clicks
        # bind_all:"<Button-1>" let us react to event of Button (click)...
        # self.mouse_click is clicked when the left-mouse is clicked
        self.bind('<Button-1>', self.mouse_click)

        # Variable to know if an active game is being played, or is over
        self.active_game = True

    def load_images(self):
        # We place this code in try-except if the images are not found (and tell us)
        try:
            # REMARK: IF WE WANT TO GENERATE EXECUTABLE, WE MUST DO THIS PATHS TO IMGS DIFFERENT!!!

            # Open the image of the body of each player's colors and robot
            self.player_1_img = Image.open(os.path.join(current_folder, "imgs", "player_1.png"))
            self.player_2_img = Image.open(os.path.join(current_folder, "imgs", "player_2.png"))
            self.robot_img = Image.open(os.path.join(current_folder, "imgs", "robot.png"))

            # Correct image dimentions that do not match window size (fix them)
            self.robot_img.thumbnail((300, 300), Image.ANTIALIAS)

            # Create the "PhotoImages" with the opened images before
            self.player_1 = ImageTk.PhotoImage(self.player_1_img)
            self.player_2 = ImageTk.PhotoImage(self.player_2_img)
            self.robot = ImageTk.PhotoImage(self.robot_img)

        except IOError as error:
            print(error)
            root.destroy()

    def create_objects(self):
        # Display my name at the top right
        self.create_text(
            350,
            25,
            text="Santiago Garcia Arango, MLH 2021",
            fill="#FFFF33",
            font=("TkDefaultFont", 15))

        # Display greetings message at the bottom
        self.create_text(
            350,
            675,
            text="Thanks for playing this amazing game by san99tiago!",
            fill="#37FFFF",
            font=("TkDefaultFont", 14))

        # We create the rectangle that gives the "boundaries" of Tic Tac Toe
        # First layer of GUI
        self.create_rectangle(50, 50, 250, 250, outline="#B8AEAB")
        self.create_rectangle(250, 50, 450, 250, outline="#B8AEAB")
        self.create_rectangle(450, 50, 650, 250, outline="#B8AEAB")

        # Second layer of GUI
        self.create_rectangle(50, 250, 250, 450, outline="#B8AEAB")
        self.create_rectangle(250, 250, 450, 450, outline="#B8AEAB")
        self.create_rectangle(450, 250, 650, 450, outline="#B8AEAB")

        # Third layer of GUI
        self.create_rectangle(50, 450, 250, 650, outline="#B8AEAB")
        self.create_rectangle(250, 450, 450, 650, outline="#B8AEAB")
        self.create_rectangle(450, 450, 650, 650, outline="#B8AEAB")

        # self.create_image(150, 150, image=self.player_1, tag="player")
        # self.create_image(350, 150, image=self.player_2, tag="player")
        # self.create_image(550, 150, image=self.player_1, tag="player")

        # self.create_image(150, 350, image=self.player_2, tag="player")
        # self.create_image(350, 350, image=self.player_1, tag="player")
        # self.create_image(550, 350, image=self.player_2, tag="player")

        # self.create_image(150, 550, image=self.player_1, tag="player")
        # self.create_image(350, 550, image=self.player_2, tag="player")
        # self.create_image(550, 550, image=self.player_1, tag="player")

    # Method to restart the game
    def on_key_press(self, event):
        # The way to restart the game
        if (event.keysym == "space" and not self.active_game):
            self.reset_game()

    # Mouse clicks
    def mouse_click(self, event):
        print("Mouse position: (%s %s)" % (event.x, event.y))
        self.move_based_on_click(event)
        return

    # Understand desired position for each click
    def move_based_on_click(self, event):
        # Default (x-y) values to check correct click
        position_x = -1
        position_y = -1

        # Check column position
        if (event.x > 50 and event.x < 250):
            print("0")
            position_y = 0
        if (event.x > 250 and event.x < 450):
            print("1")
            position_y = 1
        if (event.x > 450 and event.x < 650):
            print("2")
            position_y = 2

        # Check row position
        if (event.y > 50 and event.y < 250):
            print("0")
            position_x = 0
        if (event.y > 250 and event.y < 450):
            print("1")
            position_x = 1
        if (event.y > 450 and event.y < 650):
            print("2")
            position_x = 2

        # Apply move if it is valid
        if (position_x >= 0 and position_y >= 0):
            self.game.move([position_x, position_y])

        # Check for winner
        if self.game.check_winner() > 0:
            winner = self.game.current_player
            print("\n\nTHE WINNER IS: ", winner, "!!!!\n\n")
            self.end_game()
            self.game.restart_board()
            self.current_player = 1

    # Method for when a user wins
    def end_game(self):
        self.active_game = False

        # This Canvas inherited function allows us to delete everything from it
        self.delete(tk.ALL)

        # Show the text at the end of the game to show score
        self.create_text(
            self.winfo_width() / 2,  # Obtain half of the window-size in width
            30,
            text="Press <space> to restart",
            fill="#FFFF33",
            justify="center",
            font=("TkDefaultFont", 16))

        # Show the text at the end of the game to show score
        self.create_text(
            self.winfo_width() / 2,  # Obtain half of the window-size in width
            self.winfo_height() / 4,  # Obtain 1/4 of the window-size in height
            text="THANK YOU FOR PLAYING\nTHE BEST\nTIC-TAC-TOE GAME\n",
            fill="#FFF",
            justify="center",
            font=("TkDefaultFont", 20))

        # Show cool robot picture in the <final restart window>
        image_pos_x = self.winfo_width() / 2
        image_pos_y = 2 * self.winfo_height() / 3
        self.create_image(image_pos_x, image_pos_y, image=self.robot, tag="robot")

    def reset_game(self):
        self.active_game = True

        # This Canvas inherited function allows us to delete everything from it
        self.delete(tk.ALL)

        # Reload and initialize GUI-related things
        self.GUI_initialize()


if __name__ == "__main__":
    # Root creation and customizing it with title and NOT resizable
    root = tk.Tk()
    root.title("TIC-TAC-TOE by: san99tiago")
    root.resizable(False, False)
    # root.iconbitmap(current_folder + "\\imgs\\santa_icon.ico" )

    # Create the main Game Canvas with the class at the top...
    # (then we pack it in tkinter root)
    game = TicTacToeGUI()
    game.pack()

    # Execute main window created with tkinter
    root.mainloop()
    game = TicTacToeGUI()
    game.pack()
