#import kivy #ver check
#kivy.require("1.9.1")

__version__ = '0.19.1'

from kivy.app import App #Backbone

from kivy.lang import Builder #.kv parser
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.clock import mainthread
from functools import partial


import pyqrcode
import png

from os import listdir

class WelcomeScreen(Screen):
    def exit(self):
        quit()

class ImageButton(ButtonBehavior, Image):
	pass

class MainScreen(Screen):
    pass

class Load(Screen):
    def __init__(self,**kwargs):
        super(Load,self).__init__(**kwargs)
        self.app = App.get_running_app()
        self.app.Load = self
        self.du()
    @mainthread
    def du(self):
        app = App.get_running_app()
        user_data_dir = app.user_data_dir
        self.ids.stack.clear_widgets()
        for item in listdir(user_data_dir):
            if ".png" in item:
                button = Button(text=str(item),size_hint_x=0.2,size_hint_y=0.2)
                button.bind(on_press = partial(self.changer,item))
                self.ids.stack.add_widget(button)
    def changer(self,item,*args):
        app = App.get_running_app()
        app.root.current = "LoadButton"
        user_data_dir = app.user_data_dir
        path = user_data_dir + '/' + item
        app.LoadButton.ids.image.source = path
        #print user_data_dir + '/' + path
class LoadButton(Screen):
    def __init__(self,**kwargs):
        super(LoadButton,self).__init__(**kwargs)
        self.app = App.get_running_app()
        self.app.LoadButton = self

class BuisnessCard(Screen):
    def __init__(self,**kwargs):
        super(BuisnessCard,self).__init__(**kwargs)
        self.app = App.get_running_app()
        self.app.BuisnessCard = self

    def reload_image(self):
        app = App.get_running_app()
        w = app.CardCode.ids.image.reload()

    def qr_generator(self):
        cardname=self.cardname.text
        mobile=self.mobile.text
        home=self.home.text
        work=self.work.text
        email=self.email.text
        address=self.address.text

        app = App.get_running_app()
        user_data_dir = app.user_data_dir
        filename = app.BuisnessCard.ids.filename.text
        if filename == '':
            filename = user_data_dir + "/card_qr.png"
        else:
            filename = user_data_dir + '/' + filename + '.png'
            formatted = "Name: %s\nMobile: %s\nHome: %s\nWork: %s\nEmail: %s\nAddress: %s" %(cardname,mobile,home,work,email,address)
            inn = pyqrcode.create(formatted)
            with open(filename,'w') as inputfile:
                inn.png(inputfile,scale=10)
            self.reload_image()
            filename = user_data_dir + "/card_qr.png"
        formatted = "Name: %s\nMobile: %s\nHome: %s\nWork: %s\nEmail: %s\nAddress: %s" %(cardname,mobile,home,work,email,address)
        inn = pyqrcode.create(formatted)
        with open(filename,'w') as inputfile:
            inn.png(inputfile,scale=10)
        self.reload_image()


class Note(Screen):
    def __init__(self,**kwargs):
        super(Note,self).__init__(**kwargs)
        self.app = App.get_running_app()
        self.app.Note = self

    def reload_image(self):
        app = App.get_running_app()
        w = app.NoteCode.ids.image.reload()

    def qr_generator(self):
        app = App.get_running_app()
        user_data_dir = app.user_data_dir
        filename = app.Note.ids.filename.text
        if filename == '':
            filename = user_data_dir + "/qr.png"
        else:
            filename = user_data_dir + '/' + filename + '.png'
            note_input = app.Note.ids.note_input.text
            inn = pyqrcode.create(note_input)
            with open(filename,'w') as inputfile:
                inn.png(inputfile,scale=8)
            self.reload_image()
            #BECAUSE FUCK YOU
            filename = user_data_dir + "/qr.png"
        note_input = app.Note.ids.note_input.text
        inn = pyqrcode.create(note_input)
        with open(filename,'w') as inputfile:
            inn.png(inputfile,scale=8)
        self.reload_image()

class NoteCode(Screen):

    def __init__(self,**kwargs):
        super(NoteCode,self).__init__(**kwargs)
        self.app = App.get_running_app()
        self.app.NoteCode = self

    def path(self):
        app = App.get_running_app()
        user_data_dir = app.user_data_dir
        filename = user_data_dir + "/qr.png"

        return filename


class CardCode(Screen):
    def __init__(self,**kwargs):
        super(CardCode,self).__init__(**kwargs)
        self.app = App.get_running_app()
        self.app.CardCode = self
    def path(self):
        user_data_dir = App.get_running_app().user_data_dir
        filename = user_data_dir + "/card_qr.png"
        return filename

class ScreenManagement(ScreenManager): # Init Screens
    pass

class MainApp(App):
    def build(self):
        return ScreenManagement()

if __name__ == "__main__":
    MainApp().run()
