import tkinter as tk

class TilePiece(tk.Button):
  def __init__(self, parent, label,center=False, letter='A'):
    tk.Button.__init__(self,parent)
    self.letter = letter
    self.label = label
    #text = tk.Text(self,fg='white')
    self.config(text=self.letter,
                width=5, 
                height=3,
                command=self.select,
                padx=10,
                relief='raised',
                cursor='heart #FF0000',
                activebackground='#444443',
                background="#444443",
                fg='white',
                font=50) 
  def select(self):
    new_text = self.label.get() + self.letter
    self.label.config(text=new_text)
  def color(self,color):
    self.config(bg=color,
                activebackground=color)
  def set_letter(self, letter):
    self.letter = letter
    self.config(text=self.letter)
    self.update()
  
class WordWindow(tk.Label):
  def __init__(self, parent,start_text=None):
    tk.Label.__init__(self,parent)
    if start_text is not None:
      self.set(start_text)
    self.config(background='#232322',
                font=('helvetica', 10))
  def get(self):
    return self.cget('text')
  def set(self, text):
    self.config(text=text)
    self.update()

class ScoreWindow(tk.Text):
  def __init__(self, parent):
    tk.Text.__init__(self)
  def set(self, text):
    self.insert(tk.End, text)

class Delete(tk.Button):
  def __init__(self, parent, label):
    tk.Button.__init__(self)
    self.label = label
    self.config(text='Delete',
                command=self.delete,
                relief='raised',
                cursor='heart #FF0000',
                activebackground='#444443',
                background="#444443",
                fg='white',
                font=50)
    self.bind('<Double-Button-1>', self.delete_all)
    self.bind('<Enter')
  def delete(self):
    temp = self.label.get()
    self.label.set(text=temp[:len(temp)-1])
    self.label.update()
  def delete_all(self,event):
    self.label.set(text='')
    self.label.update()
    
class Submit(tk.Button):
  def __init__(self, parent, label, game, user_input, center_letter, score):
    self.game = game
    self.accepted = user_input
    self.center_letter = center_letter
    self.score = score
    tk.Button.__init__(self)
    self.label = label
    self.config(text='Enter',
                command=self.submit,
                relief='raised',
                cursor='heart #FF0000', 
                activebackground='#444443', 
                background="#444443",
                fg='white',
                font=50)
  def submit(self):
    input = self.label.get().lower()
    if self.center_letter.lower() in input:
      result = self.game.check_valid(input)
      if result:
        self.accepted.set(
          self.game.get_user_entry_words())
        self.accepted.update()
        curr = int(self.score.get())
        new = 0
        if len(input) == 4:
          new = curr + 4
        elif len(input) == 5:
          new = curr + 6
        elif len(input) == 6:
          new = curr + 8
        elif len(input) > 6:
          new = curr + 11
        self.score.set(new)

      if result is None:
        curr = int(self.score.get())
        new = curr + 20
        self.score.config(fg='green')
        self.score.set(new)
        self.score.update()
    self.label.set('')
    self.label.update()
  def cheats(self,event):
    self.score.set(self.game.word_of_day)