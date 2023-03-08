from tkinter import *
from PIL import Image, ImageTk
from random import randint
import Robot
import Persona

class GUIPiedras:

    def __init__(self):
        # Ventana pricipal
        self.root = Tk()
        self.root.title("Piedra, Papel, Tijera, Lagarto y Spock")
        self.root.configure(background="#1A237E")
        # Imagenes
        self.rock_img = ImageTk.PhotoImage(Image.open("piedra-usuario.png"))
        self.rock_img_pc = ImageTk.PhotoImage(Image.open("piedra-pc.png"))
        self.paper_img = ImageTk.PhotoImage(Image.open("papel-usuario.png"))
        self.paper_img_pc = ImageTk.PhotoImage(Image.open("papel-pc.png"))
        self.scissors_img = ImageTk.PhotoImage(Image.open("tijeras-usuario.png"))
        self.scissors_img_pc = ImageTk.PhotoImage(Image.open("tijeras-pc.png"))
        self.lizard_img = ImageTk.PhotoImage(Image.open("lagarto-usuario.png"))
        self.lizard_img_pc = ImageTk.PhotoImage(Image.open("lagarto-pc.png"))
        self.spock_img = ImageTk.PhotoImage(Image.open("spock-usuario.png"))
        self.spock_img_pc = ImageTk.PhotoImage(Image.open("spock-pc.png"))

        # Insertar imágenes a la ventana
        self.user_label = Label(self.root, image=self.scissors_img, bg="#1A237E")
        self.pc_label = Label(self.root, image=self.scissors_img_pc, bg="#1A237E")
        self.user_label.grid(row=1, column=0)
        self.pc_label.grid(row=1, column=6)

        # Puntajes
        self.playerScore = Label(self.root, text=0, font=100, bg="#1A237E", fg="white")
        self.computerScore = Label(self.root, text=0, font=100, bg="#1A237E", fg="white")
        self.computerScore.grid(row=1, column=3)
        self.tieScore = Label(self.root, text=0, font=100, bg="#1A237E", fg="white")
        self.tieScore.grid(row=1, column=2)
        self.playerScore.grid(row=1, column=1)

        # Indicadores
        self.user_indicator = Label(self.root, font=100, text="USUARIO", bg="#1A237E", fg="white")
        self.pc_indicator = Label(self.root, font=100, text="COMPUTADORA", bg="#1A237E", fg="white")
        self.tie_indicator = Label(self.root, font=100, text="EMPATE", bg="#1A237E", fg="white")
        self.user_indicator.grid(row=0, column=1)
        self.tie_indicator.grid(row=0, column=2)
        self.pc_indicator.grid(row=0, column=3)

        # Mensajes
        self.msg = Label(self.root, font=50, bg="#1A237E", fg="white", text="")
        self.msg.grid(row=3, column=2)

        # Botones
        button_font = ("Helvetica", 11, "bold")
        button_color = "#3498db"
        button_hover_color = "#2980b9"
        button_fg = "white"

        self.rock = Button(self.root, width=15, height=2, text="Piedra",
                           bg=button_color, fg=button_fg, font=button_font,
                           activebackground=button_hover_color, command=lambda: self.updateChoice("piedra")).grid(row=2,
                                                                                                                  column=1)
        self.scissors = Button(self.root, width=16, height=2, text="Tijera",
                               bg=button_color, fg=button_fg, font=button_font,
                               activebackground=button_hover_color, command=lambda: self.updateChoice("tijeras")).grid(
            row=2,
            column=2)
        self.paper = Button(self.root, width=15, height=2, text="Papel",
                            bg=button_color, fg=button_fg, font=button_font,
                            activebackground=button_hover_color, command=lambda: self.updateChoice("papel")).grid(row=2,
                                                                                                                  column=3)
        self.lizard = Button(self.root, width=15, height=2, text="Lagarto",
                             bg=button_color, fg=button_fg, font=button_font,
                             activebackground=button_hover_color, command=lambda: self.updateChoice("lagarto")).grid(
            row=3,
            column=1)
        self.spock = Button(self.root, width=15, height=2, text="Spock",
                            bg=button_color, fg=button_fg, font=button_font,
                            activebackground=button_hover_color, command=lambda: self.updateChoice("spock")).grid(row=3,
                                                                                                                  column=3)


        self.contador = 0
        self.robotina = Robot.Robot()
        self.yo = Persona.Persona()
        self.empates = 0
        self.tiradas = {'piedra': [0, ('tijeras', 'lagarto')],
                        'papel': [0, ('piedra', 'spock')],
                        'tijeras': [0, ('papel', 'lagarto')],
                        'lagarto': [0, ('spock', 'papel')],
                        'spock': [0, ('piedra', 'tijeras')]}
        self.root.mainloop()
    # Actualiza el mensaje
    def updateMessage(self, x):
        self.msg['text'] = x

    # Actualiza el puntaje de el usuario
    def updateUserScore(self):
        score = int(self.playerScore["text"])
        score += 1
        self.playerScore["text"] = str(score)

    # Actualiza el puntaje de la computadora
    def updatePCScore(self):
        score = int(self.computerScore["text"])
        score += 1
        self.computerScore["text"] = str(score)

    def updateTieScore(self):
        score = int(self.tieScore["text"])
        score += 1
        self.tieScore["text"] = str(score)
    # Actualiza las respuestas

    def updateChoice(self, x):
        self.yo.tirada = x
        pcChoice = self.robotina.tirar(self.tiradas, self.contador)
        if x == "piedra":
            self.user_label.configure(image=self.rock_img)
        elif x == "papel":
            self.user_label.configure(image=self.paper_img)
        elif x == "spock":
            self.user_label.configure(image=self.spock_img)
        elif x == "lagarto":
            self.user_label.configure(image=self.lizard_img)
        elif x == "tijeras":
            self.user_label.configure(image=self.scissors_img)

        if pcChoice == "piedra":
            self.pc_label.configure(image=self.rock_img_pc)
        if pcChoice == "papel":
            self.pc_label.configure(image=self.paper_img_pc)
        if pcChoice == "tijeras":
            self.pc_label.configure(image=self.scissors_img_pc)
        if pcChoice == "lagarto":
            self.pc_label.configure(image=self.lizard_img_pc)
        if pcChoice == "spock":
            self.pc_label.configure(image=self.spock_img_pc)

        if self.yo.tirada in self.tiradas[self.robotina.tirada][1]:
            self.updateMessage("Ganó robotina")
            self.updatePCScore()
            self.robotina.victorias += 1
        elif self.yo.tirada == self.robotina.tirada:
            self.updateMessage("Empataron")
            self.updateTieScore()
            self.empates += 1
        else:
            self.updateMessage("Ganó usted")
            self.updateUserScore()
            self.yo.victorias += 1
        self.contador += 1
        self.tiradas[self.yo.tirada][0] += 1
        print("Robotina ", self.robotina.victorias, " Usuario ", self.yo.victorias, " Empates ", self.empates)
