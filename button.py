from kivy.app import App
from kivy.uix.button import Button
# from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout    
from kivy.uix.image import Image    
from kivy.core.window import Window
from kivy.clock import Clock
# from callback import Callback
from callback import speedDecrease, speedIncrease, getSpeed
from BertecMan_Mod import Bertec
import winsound
import time
    
class ButtonApp(App):
    """
    Button class, defines all GUI properties
    """    
    def build(self):
        Window.clearcolor = (202/255, 217/255, 206/255, 1)
        
        superBox = BoxLayout(orientation='vertical')
        MiddleBox = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, 0.2), padding=10)

        btn2 = Button(text ="–",
                   font_size ="100sp",
                   background_color =(1, 0, 0, 0.9),
                   color =(1, 1, 1, 1),
                   size =(32, 32),
                   size_hint =(1, 0.4))
        
        btn1 = Button(text ="+",
                   font_size ="100sp",
                   background_color =(22/255, 231/255, 22/255, 0.9),
                   color =(1, 1, 1, 1),
                   size =(32, 32),
                   size_hint =(1, 0.4))
 
        btn1.bind(on_press = self.callback1)
        btn2.bind(on_press = self.callback2)

        Locolab_logo = Image(source='Logo.jpg', size_hint=(1, 1))
        MiddleBox.add_widget(Button(background_color =(202/255, 217/255, 206/255, 0)))
        MiddleBox.add_widget(Locolab_logo)
        MiddleBox.add_widget(Button(background_color =(202/255, 217/255, 206/255, 0)))

        superBox.add_widget(btn1)
        superBox.add_widget(MiddleBox)
        superBox.add_widget(btn2)

        Clock.schedule_interval(self.getSpeed, 0.5)

        return superBox

    def on_start(self):
        self.bertecObj = Bertec()
        self.bertecObj.start()
        winsound.PlaySound('ringtone.wav', winsound.SND_FILENAME)
        # winsound.Beep(800, 2500)        # Just a beep sound to indicate the treadmill will speedup
        time.sleep(0.5)
        self.bertecObj._write_command(0.5, 0.5)
        print('Bertec communication set up')

    def on_stop(self):
        winsound.Beep(800, 1000)        # Just a beep sound to indicate the treadmill will slowdown
        time.sleep(0.5)
        self.bertecObj._write_command(0, 0)
        self.bertecObj.stop()
        print('Bertec communication closed')
 
    # callback function tells when button pressed
    def callback1(self, event):
        speedIncrease(self.bertecObj)

    def callback2(self, event):
        speedDecrease(self.bertecObj)

    def getSpeed(self, event):
        currentSpeed = getSpeed(self.bertecObj)
        print("Current speed: %.2f m/s" %currentSpeed, end='\r')

if __name__ == '__main__':
    ButtonApp().run()