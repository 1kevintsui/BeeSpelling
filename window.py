import tkinter as Tk
from gamepieces import TilePiece, \
WordWindow, Delete, Submit
from spelling_game import SpellingGame
import random as rand

class Window(Tk.Tk):
  def __init__(self):
    super().__init__()
    self.game = SpellingGame()
    self.title("Bee Spelling")
    self.geometry("400x500")
    self.wm_attributes('-type', 'splash')
    self.config(background='#232322')
    self.columnconfigure(0, weight=1)
    self.columnconfigure(1, weight=1)
    self.columnconfigure(2, weight=1)
    # row 0 is for the score
    self.rowconfigure(0, weight=2)
    # row 1 is for the current accepted words
    self.rowconfigure(1, weight=1)
    # row 2 is for the current typed word
    self.rowconfigure(2, weight=1)
    # row 3 is for the first 2 buttons
    self.rowconfigure(3, weight=1)
    # row 4 is for the middle 3 buttons
    self.rowconfigure(4, weight=1)
    # row 5 is for the last 2 buttons
    self.rowconfigure(5, weight=1)
    # row 6 will be for delete, refresh, submit
    self.rowconfigure(6, weight=1)
    
    self.score = WordWindow(self)
    self.score.config(text=0)
    self.accepted = WordWindow(self)
    self.label = WordWindow(self)
    self.label.config(font=30,
                      borderwidth=3,
                      relief="solid",
                      fg='white',
                      background='#444443')
    self.accepted.config(font=20,
                         borderwidth=3,
                         relief="solid",
                         fg='white',
                         background='#444443')
    self.score.config(font=50,
                      fg='white',
                      borderwidth=3)

    self.score.grid(row=0,
                    columnspan=3,
                    sticky='nsew')
    self.accepted.grid(row=1,
                       columnspan=3,
                       sticky='ew')
    self.label.grid(row=2, 
                    columnspan=3, 
                    sticky='ew')
    
    button_frame = Tk.Frame(self, bg='#232322')
    button_frame.rowconfigure(0, weight=1)
    button_frame.rowconfigure(1, weight=1)
    button_frame.rowconfigure(2, weight=1)
    button_frame.grid(row=4,columnspan=3)
    
    top_buttons = Tk.Frame(button_frame, bg='#232322')
    top_buttons.columnconfigure(0, weight=1)
    top_buttons.columnconfigure(1, weight=1)
    top_buttons.grid(row=0)
    
    mid_buttons = Tk.Frame(button_frame, bg='#232322')
    mid_buttons.columnconfigure(0, weight=1)
    mid_buttons.columnconfigure(1, weight=1)
    mid_buttons.columnconfigure(2, weight=1)
    mid_buttons.grid(row=1)

    bot_buttons = Tk.Frame(button_frame, bg='#232322')
    bot_buttons.columnconfigure(0, weight=1)
    bot_buttons.columnconfigure(1, weight=1)
    bot_buttons.grid(row=2)

    self.buttons = [
      TilePiece(mid_buttons, self.label, True),
      TilePiece(top_buttons, self.label),
      TilePiece(top_buttons, self.label),
      TilePiece(mid_buttons, self.label),
      TilePiece(mid_buttons, self.label),
      TilePiece(bot_buttons, self.label),
      TilePiece(bot_buttons, self.label)
    ]
    self.buttons[0].color('yellow')
    self.buttons[0].config(fg='black')
    # top row
    self.buttons[1].grid(row=0, column=0)
    self.buttons[2].grid(row=0, column=1)
    # middle row
    self.buttons[3].grid(row=0,column=0)
    self.buttons[0].grid(row=0,column=1)
    self.buttons[4].grid(row=0,column=2)
    # bottom row
    self.buttons[5].grid(row=0,column=0)
    self.buttons[6].grid(row=0,column=1)
    
    self.letters = self.game.letters()
    main_letter_num = rand.randint(0,len(self.letters)-1)
    main_letter = self.letters[main_letter_num].upper()
    self.buttons[0].set_letter(main_letter)
    self.buttons[0].update()
    self.new_letters = self.letters
    self.new_letters.remove(main_letter.lower())
    for i in range(0, len(self.new_letters)):
      self.buttons[i+1].set_letter(self.new_letters[i].upper())
      self.buttons[i].update()
    self.delete = Delete(self, self.label)
    self.submit = Submit(self, self.label, self.game, self.accepted, main_letter,self.score)

    self.delete.grid(row=5, column=0)
    self.submit.grid(row=5, column=2)

    self.shuffle = Tk.Button(self, 
                             text="Shuffle",
                             command=self.shuffle)
    self.shuffle.config(relief='raised',
                        cursor='heart #FF0000',
                        activebackground='#444443',
                        background="#444443",
                        fg='white',
                        font=50)
    self.shuffle.grid(row=5, column=1)
    def cheats(e):
      self.score.set(self.game.word_of_day)
    self.score.bind('<Triple-1>', cheats)
    self.update()
  def shuffle(self):
    rand.shuffle(self.new_letters)
    for i in range(0, len(self.new_letters)):
      self.buttons[i+1].set_letter(self.new_letters[i].upper())
    self.buttons[i].update()
    self.update()
    