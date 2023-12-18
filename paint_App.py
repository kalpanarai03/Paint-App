from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scatter import Scatter
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color, Line, Ellipse
from kivy.core.window import Window
Window.show_cursor = False

class DrawingWidget(Widget):
    def __init__(self):
        Window.bind(mouse_pos=self.on_mouse_pos)
        super(DrawingWidget, self).__init__()

        with self.canvas:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            Color(0,0,0)
            Rectangle(size=(400,200), pos=(0,0))
        self.bind(pos=self.update_rectangle, size=self.update_rectangle)
        
        self.color = [0,0,0]
        self.color_grid = GridLayout(cols=2, size=(400,200), pos=(0,0))
        self.label = Label(text='CC')
        self.color_grid.add_widget(self.label)
        self.label = Label(text='  ')
        self.color_grid.add_widget(self.label)
        self.label = Label(text='Red')
        self.color_grid.add_widget(self.label)
        self.red = Slider(min=0, max=100)
        self.red.bind(value = self.change_red)
        self.color_grid.add_widget(self.red)
        self.label = Label(text='Green')
        self.color_grid.add_widget(self.label)
        self.green = Slider(min=0, max=100)
        self.green.bind(value = self.change_green)
        self.color_grid.add_widget(self.green)
        self.label = Label(text='Blue')
        self.color_grid.add_widget(self.label)
        self.blue = Slider(min=0, max=100)
        self.blue.bind(value = self.change_blue)
        self.color_grid.add_widget(self.blue)
        self.add_widget(self.color_grid)

        with self.canvas:
            Color(0,0,0)
            self.mouse = Ellipse(pos=(410,210), size=(10,10))

    def change_red(self, instance, value):
        self.color[0] = int(value)/100
        self.remove_widget(self.color_grid)
        with self.canvas:
            Color(0,0,0)
            Rectangle(size=(400,200), pos=(0,0))
            Color(*self.color)
            Rectangle(size=(200,40), pos=(200,150))
        self.add_widget(self.color_grid)
        with self.canvas:
            Color(*self.color)
            self.mouse = Ellipse(pos=self.mouse.pos, size=(10,10))

    def change_green(self, instance, value):
        self.color[1] = int(value)/100
        self.remove_widget(self.color_grid)
        with self.canvas:
            Color(0,0,0)
            Rectangle(size=(400,200), pos=(0,0))
            Color(*self.color)
            Rectangle(size=(200,40), pos=(200,150))
        self.add_widget(self.color_grid)
        with self.canvas:
            Color(*self.color)
            self.mouse = Ellipse(pos=self.mouse.pos, size=(10,10))

    def change_blue(self, instance, value):
        self.color[2] = int(value)/100
        self.remove_widget(self.color_grid)
        with self.canvas:
            Color(0,0,0)
            Rectangle(size=(400,200), pos=(0,0))
            Color(*self.color)
            Rectangle(size=(200,40), pos=(200,150))
        self.add_widget(self.color_grid)
        with self.canvas:
            Color(*self.color)
            self.mouse = Ellipse(pos=self.mouse.pos, size=(10,10))

    def update_rectangle(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_touch_down(self, touch):
        super(DrawingWidget, self).on_touch_down(touch)

        if(touch.pos[1]<205 and touch.pos[0]<405):
            pass
        else:
            with self.canvas:
                Color(*self.color)
                self.line = Line(points=[touch.pos[0], touch.pos[1]], width=2)

    def on_touch_move(self, touch):
        try:
            if(touch.pos[1]<205 and touch.pos[0]<405):
                self.line.points = self.line.points + [405, 205]
            else:
                self.line.points = self.line.points + [touch.pos[0], touch.pos[1]]
        except:
            pass

    def on_touch_up(self, touch):
        try:
            del self.line
        except:
            pass

    def on_mouse_pos(self, *args):
        x,y = args[1]
        self.mouse.pos = [x,y]


class DrawingApp(App):

    def build(self):
        root_widget = DrawingWidget()
        return root_widget

DrawingApp().run()
