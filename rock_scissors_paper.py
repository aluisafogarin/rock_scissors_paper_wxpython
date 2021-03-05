import wx 
from random import randrange

class Window(wx.Frame):
    user_choice = None
    computer_choice = None

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.basic_gui()
        self.Show(True)

    def basic_gui(self):
        panel = wx.Panel(self)

        self.CreateStatusBar()
        self.SetStatusText('Rock, scissors, paper')

        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()

        aboutItem = fileMenu.Append(wx.ID_ABOUT, 'About', 'About the application')
        exitItem = fileMenu.Append(wx.ID_EXIT, 'Exit', 'Close the application')

        menuBar.Append(fileMenu, '&File')
        text = wx.StaticText(panel, -1, 'Choose your move!', (180, 30))

        button_one = wx.Button(panel, 1, 'Rock', (195, 50))
        button_two = wx.Button(panel, 2, 'Scissors', (195, 100))
        button_three = wx.Button(panel, 3, 'Paper', (195, 150))

        self.Bind(wx.EVT_MENU, self.on_exit, exitItem)
        self.Bind(wx.EVT_MENU, self.on_about, aboutItem)
        
        self.Bind(wx.EVT_BUTTON, self.on_rock, button_one)
        self.Bind(wx.EVT_BUTTON, self.on_scissors, button_two)
        self.Bind(wx.EVT_BUTTON, self.on_paper, button_three)

        self.SetTitle('Rock, scissors, paper')
        self.SetMenuBar(menuBar)
        self.SetSize(500,300)
        self.Centre()

    def result_gui(self, result):
        if result == True:
            result_dialog = wx.MessageDialog(None, f"You choose {self.user_choice}, computer choose {self.computer_choice}.You won :)\nWanna play again?", "Result", wx.YES_NO)
        
        elif result == False:
            result_dialog = wx.MessageDialog(None, f"You choose {self.user_choice}, computer choose {self.computer_choice}. You lost :(\nWanna play again?", "Result", wx.YES_NO)
        
        else:
            result_dialog = wx.MessageDialog(None, f"You and computer choose {self.user_choice}! Tie!\nWanna play again?", "Result", wx.YES_NO)

        if result_dialog.ShowModal() == wx.ID_YES:
            result_dialog.Destroy()
        else:
            self.Close()

    def on_rock(self, event):
        self.user_choice = 'rock'
        self.play()

    def on_scissors(self, event):
        self.user_choice = 'scissors'
        self.play()

    def on_paper(self, event):
        self.user_choice = 'paper'
        self.play()

    def play(self):
        num = randrange(1,4)

        if num == 1:
            self.computer_choice = 'rock'
        elif num == 2:
            self.computer_choice = 'scissors'
        elif num == 3:
            self.computer_choice = 'paper'

        if self.user_choice == self.computer_choice:
            self.result_gui(None)

        if self.user_choice == 'paper' and self.computer_choice == 'rock':
            self.result_gui(True)
        
        if self.user_choice == 'scissors' and self.computer_choice == 'paper':
            self.result_gui(True)

        if self.user_choice == 'rock' and self.computer_choice == 'scissors':
            self.result_gui(True)

        if self.computer_choice == 'paper' and self.user_choice == 'rock':
            self.result_gui(False)

        if self.computer_choice == 'scissors' and self.user_choice == 'paper':
            self.result_gui(False)

        if self.computer_choice == 'rock' and self.user_choice == 'scissors':
            self.result_gui(False)  

    def on_exit(self, event):
        self.Close()

    def on_about(self, event):
        aboutDialog = wx.MessageDialog(None, "This is a rock, scissors and paper game. Choose one, and see if you're lucky!", "About", wx.OK)
        if aboutDialog.ShowModal() == wx.ID_OK:
            aboutDialog.Destroy()

def main():
    app = wx.App()
    Window(None)
    app.MainLoop()

main()