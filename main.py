from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from random import randint
from kivy.core.audio import Sound
from kivy.core.audio import SoundLoader


class MyApp(App):

    def __init__(self):
        super().__init__()
        self.wind = str(Window.size)
        self.wid = int(self.wind[1:self.wind.find(',')])
        self.hei = int(self.wind[self.wind.find(' ') + 1:-1])
        self.btn01 = Button(text='Обычная игра', font_size=30, pos=(self.wid*0.25, self.hei*0.501),
                            size_hint=(0.5, 0.15*(self.wid/self.hei)),
                            background_color=[0, 1, 0, 1], background_normal='')
        self.btn01.color = [0, 0, 1, 1]
        self.btn01.bind(on_press=self.pressed_start)
        self.btn02 = Button(text='Генератор', font_size=30, pos=(self.wid*0.25, self.hei*(0.5-0.151*(self.wid/self.hei))),
                            size_hint=(0.5, 0.15*(self.wid/self.hei)),
                            background_color=[0, 0, 1, 1], background_normal='')
        self.btn02.color = [0, 1, 0, 1]
        self.btn02.bind(on_press=self.pressed_generate)
        self.btns = []
        self.btns.append(self.btn02)
        self.fl = FloatLayout()
        self.btn2id = 0
        self.btn_res = 0
        self.anch_res = AnchorLayout(anchor_x='left', anchor_y='top')
        self.anch_ex = AnchorLayout(anchor_x='right', anchor_y='top')
        self.anch_hide = AnchorLayout(anchor_x='left', anchor_y='bottom')
        self.btn_hide = 0
        self.btn_ex = Button(text='×', font_size=30, background_color=[1, 0, 0, 1], background_normal='',
                             size_hint=(0.07, 0.07*(self.wid/self.hei)))
        self.btn_ex.bind(on_press=self.pressed_exit)
        self.check = 1
        self.gen = 1
        self.text = TextInput(font_size=30, multiline=False, is_focusable=True)
        self.text.background_color = [1, 1, 1, 1]
        self.text.foreground_color = [0, 1, 0, 1]
        self.text.pos = (self.wid * 0.25, self.hei * 0.501)
        self.text.size_hint = (0.5, 0.15 * (self.wid / self.hei))
        self.text.halign = 'center'
        self.text.bind(on_text_validate=self.text_generate)
        self.btn_gen = Button(text='Сгенерировать', font_size=30,
                              pos=(self.wid * 0.25, self.hei * (0.5 - 0.151 * (self.wid / self.hei))),
                              size_hint=(0.5, 0.15 * (self.wid / self.hei)),
                              background_color=[0, 1, 0, 1], background_normal='')
        self.btn_gen.bind(on_press=self.generating)
        self.btn_menu = Button(text='Меню', font_size=30,
                               pos=(self.wid * 0.43, 0),
                               size_hint=(0.14, 0.07 * (self.wid / self.hei)),
                               background_color=[0.7, 0.7, 0.7, 1], background_normal='')
        self.btn_menu.bind(on_press=self.pressed_menu)
        self.btn_res = Button(text='0', font_size=30, background_color=[0.5, 0.5, 0.5, 1], background_normal='',
                              size_hint=(0.07, 0.07 * (self.wid / self.hei)))
        self.btn_res.bind(on_press=self.pressed_restart)
        self.sound = SoundLoader.load('Twilig.mp3')
        self.sound.play()
        Sound.loop = True

    def build(self):
        self.fl.add_widget(self.btn01)
        self.fl.add_widget(self.btn02)
        self.anch_ex.add_widget(self.btn_ex)
        self.anch_res.add_widget(self.btn_res)
        self.fl.add_widget(self.anch_ex)
        self.fl.add_widget(self.anch_res)
        return self.fl

    def pressed_start(self, z):
        self.fl.remove_widget(self.btn01)
        self.fl.remove_widget(self.btn02)
        self.fl.remove_widget(self.btns[0])
        self.btns.remove(self.btns[0])
        btn = Button(text='',
                     pos=(randint(0, int(self.wid*0.95)),
                          randint(int(self.hei*0.1), int(self.hei*(1-0.12*(self.wid/self.hei))))),
                     size_hint=(0.05, 0.05*(self.wid/self.hei)),
                     background_color=[randint(0, 255)/255, randint(0, 255)/255, randint(0, 255)/255, 1],
                     background_normal='')
        btn.bind(on_press=self.pressed_start)
        self.btns.append(btn)
        self.fl.add_widget(btn)
        secbtn = randint(0, 25)
        if secbtn == 5:
            btn2 = Button(text='',
                          pos=(randint(0, int(self.wid*0.95)),
                               randint(int(self.hei*0.1), int(self.hei*(1-0.12*(self.wid/self.hei))))),
                          size_hint=(0.05, 0.05*(self.wid/self.hei)),
                          background_color=[randint(0, 255)/255, randint(0, 255)/255, randint(0, 255)/255, 1],
                          background_normal='')
            btn2.bind(on_press=self.pressed_start2)
            self.btn2id = len(self.btns)-1
            self.btns.append(btn2)
            self.fl.add_widget(btn2)
        fon = randint(0, 10)
        if fon == 5:
            Window.clearcolor = [randint(0, 255)/255, randint(0, 255)/255, randint(0, 255)/255, 1]
        self.btn_hide = Button(text='', background_color=Window.clearcolor, background_normal='',
                               size_hint=(0.07, 0.07 * (self.wid / self.hei)))
        self.btn_hide.bind(on_press=self.pressed_hide)
        self.anch_hide.add_widget(self.btn_hide)
        if self.check == 1:
            count = str(len(self.btns))
            self.anch_res.remove_widget(self.btn_res)
            self.fl.remove_widget(self.anch_res)
            self.btn_res = Button(text=count, font_size=30, background_color=[0.5, 0.5, 0.5, 1], background_normal='',
                                  size_hint=(0.06+len(count)*0.01, 0.07 * (self.wid / self.hei)))
            self.btn_res.bind(on_press=self.pressed_restart)
            self.anch_res.add_widget(self.btn_res)
            self.fl.add_widget(self.anch_res)
            self.fl.remove_widget(self.anch_ex)
            self.fl.add_widget(self.anch_ex)
            self.fl.remove_widget(self.btn_menu)
            self.fl.add_widget(self.btn_menu)
        self.fl.remove_widget(self.anch_hide)
        self.fl.add_widget(self.anch_hide)
        return self.fl

    def pressed_start2(self, z):
        self.fl.remove_widget(self.btns[self.btn2id])
        self.btns.remove(self.btns[self.btn2id])
        btn = Button(text='',
                     pos=(randint(0, int(self.wid * 0.95)),
                          randint(int(self.hei*0.1), int(self.hei * (1 - 0.12 * (self.wid / self.hei))))),
                     size_hint=(0.05, 0.05 * (self.wid / self.hei)),
                     background_color=[randint(0, 255) / 255, randint(0, 255) / 255, randint(0, 255) / 255, 1],
                     background_normal='')
        btn.bind(on_press=self.pressed_start)
        self.btns.append(btn)
        self.fl.add_widget(btn)
        secbtn = randint(0, 25)
        if secbtn == 5:
            btn2 = Button(text='',
                          pos=(randint(0, int(self.wid * 0.95)),
                               randint(int(self.hei*0.1), int(self.hei * (1 - 0.12 * (self.wid / self.hei))))),
                          size_hint=(0.05, 0.05 * (self.wid / self.hei)),
                          background_color=[randint(0, 255) / 255, randint(0, 255) / 255, randint(0, 255) / 255, 1],
                          background_normal='')
            btn2.bind(on_press=self.pressed_start2)
            self.btn2id = len(self.btns) - 1
            self.btns.append(btn2)
            self.fl.add_widget(btn2)
        fon = randint(1, 10)
        if fon == 5:
            Window.clearcolor = [randint(0, 255) / 255, randint(0, 255) / 255, randint(0, 255) / 255, 1]
        self.btn_hide = Button(text='', background_color=Window.clearcolor, background_normal='',
                               size_hint=(0.07, 0.07 * (self.wid / self.hei)))
        self.btn_hide.bind(on_press=self.pressed_hide)
        self.anch_hide.add_widget(self.btn_hide)
        if self.check == 1:
            count = str(len(self.btns))
            self.anch_res.remove_widget(self.btn_res)
            self.fl.remove_widget(self.anch_res)
            self.btn_res = Button(text=count, font_size=30, background_color=[0.5, 0.5, 0.5, 1], background_normal='',
                                  size_hint=(0.06+len(count)*0.01, 0.07 * (self.wid / self.hei)))
            self.btn_res.bind(on_press=self.pressed_restart)
            self.anch_res.add_widget(self.btn_res)
            self.fl.add_widget(self.anch_res)
            self.fl.remove_widget(self.anch_ex)
            self.fl.add_widget(self.anch_ex)
            self.fl.remove_widget(self.btn_menu)
            self.fl.add_widget(self.btn_menu)
        self.fl.remove_widget(self.anch_hide)
        self.fl.add_widget(self.anch_hide)
        return self.fl

    def pressed_exit(self, z):
        Window.close()

    def pressed_restart(self, z):
        self.fl.remove_widget(self.btn01)
        self.fl.remove_widget(self.btn02)
        self.fl.remove_widget(self.text)
        self.fl.remove_widget(self.btn_gen)
        for i in range(len(self.btns)):
            self.fl.remove_widget(self.btns[0])
            self.btns.remove(self.btns[0])
        Window.clearcolor = [0, 0, 0, 1]
        btn = Button(text='',
                     pos=(randint(0, int(self.wid * 0.95)),
                          randint(int(self.hei * 0.1), int(self.hei * (1 - 0.12 * (self.wid / self.hei))))),
                     size_hint=(0.05, 0.05 * (self.wid / self.hei)),
                     background_color=[randint(0, 255) / 255, randint(0, 255) / 255, randint(0, 255) / 255, 1],
                     background_normal='')
        btn.bind(on_press=self.pressed_start)
        self.btns.append(btn)
        self.fl.add_widget(btn)
        self.btn_hide = Button(text='', background_color=Window.clearcolor, background_normal='',
                               size_hint=(0.07, 0.07 * (self.wid / self.hei)))
        self.btn_hide.bind(on_press=self.pressed_hide)
        self.anch_hide.add_widget(self.btn_hide)
        if self.check == 1:
            count = str(len(self.btns))
            self.anch_res.remove_widget(self.btn_res)
            self.fl.remove_widget(self.anch_res)
            self.btn_res = Button(text=count, font_size=30, background_color=[0.5, 0.5, 0.5, 1], background_normal='',
                                  size_hint=(0.06+len(count)*0.01, 0.07 * (self.wid / self.hei)))
            self.btn_res.bind(on_press=self.pressed_restart)
            self.anch_res.add_widget(self.btn_res)
            self.fl.add_widget(self.anch_res)
            self.fl.remove_widget(self.anch_ex)
            self.fl.add_widget(self.anch_ex)
            self.fl.remove_widget(self.btn_menu)
            self.fl.add_widget(self.btn_menu)
        return self.fl

    def pressed_hide(self, z):
        if self.check == 1:
            self.anch_res.remove_widget(self.btn_res)
            self.fl.remove_widget(self.anch_res)
            self.fl.remove_widget(self.anch_ex)
            self.fl.remove_widget(self.btn_menu)
            self.check = 0
        else:
            count = str(len(self.btns))
            self.anch_res.remove_widget(self.btn_res)
            self.fl.remove_widget(self.anch_res)
            self.btn_res = Button(text=count, font_size=30, background_color=[0.5, 0.5, 0.5, 1], background_normal='',
                                  size_hint=(0.06+len(count)*0.01, 0.07 * (self.wid / self.hei)))
            self.btn_res.bind(on_press=self.pressed_restart)
            self.anch_res.add_widget(self.btn_res)
            self.fl.add_widget(self.anch_res)
            self.fl.remove_widget(self.anch_ex)
            self.fl.add_widget(self.anch_ex)
            self.fl.remove_widget(self.btn_menu)
            self.fl.add_widget(self.btn_menu)
            self.check = 1

    def pressed_generate(self, z):
        self.fl.remove_widget(self.btn01)
        self.fl.remove_widget(self.btn02)
        self.fl.add_widget(self.text)
        self.fl.add_widget(self.btn_gen)
        return self.fl

    def text_generate(self, gen):
        self.gen = int(gen.text)

    def generating(self, z):
        self.fl.remove_widget(self.text)
        self.fl.remove_widget(self.btn_gen)
        for i in range(self.gen-1):
            btn = Button(text='',
                         pos=(randint(0, int(self.wid * 0.95)),
                              randint(int(self.hei * 0.1), int(self.hei * (1 - 0.12 * (self.wid / self.hei))))),
                         size_hint=(0.05, 0.05 * (self.wid / self.hei)),
                         background_color=[randint(0, 255) / 255, randint(0, 255) / 255, randint(0, 255) / 255, 1],
                         background_normal='')
            btn.bind(on_press=self.pressed_start)
            self.btns.append(btn)
            self.fl.add_widget(btn)
        self.btn_hide = Button(text='', background_color=Window.clearcolor, background_normal='',
                               size_hint=(0.07, 0.07 * (self.wid / self.hei)))
        self.btn_hide.bind(on_press=self.pressed_hide)
        self.anch_hide.add_widget(self.btn_hide)
        if self.check == 1:
            count = str(len(self.btns))
            self.anch_res.remove_widget(self.btn_res)
            self.fl.remove_widget(self.anch_res)
            self.btn_res = Button(text=count, font_size=30, background_color=[0.5, 0.5, 0.5, 1], background_normal='',
                                  size_hint=(0.06+len(count)*0.01, 0.07 * (self.wid / self.hei)))
            self.btn_res.bind(on_press=self.pressed_restart)
            self.anch_res.add_widget(self.btn_res)
            self.fl.add_widget(self.anch_res)
            self.fl.remove_widget(self.anch_ex)
            self.fl.add_widget(self.anch_ex)
            self.fl.remove_widget(self.btn_menu)
            self.fl.add_widget(self.btn_menu)
        self.fl.remove_widget(self.anch_hide)
        self.fl.add_widget(self.anch_hide)
        Window.clearcolor = [randint(0, 255)/255, randint(0, 255)/255, randint(0, 255)/255, 1]
        return self.fl

    def pressed_menu(self, z):
        self.fl.remove_widget(self.btn_menu)
        for i in range(len(self.btns)):
            self.fl.remove_widget(self.btns[0])
            self.btns.remove(self.btns[0])
        count = str(len(self.btns))
        self.anch_res.remove_widget(self.btn_res)
        self.fl.remove_widget(self.anch_res)
        self.btn_res = Button(text=count, font_size=30, background_color=[0.5, 0.5, 0.5, 1], background_normal='',
                              size_hint=(0.06+len(count)*0.01, 0.07 * (self.wid / self.hei)))
        self.btn_res.bind(on_press=self.pressed_restart)
        self.anch_res.add_widget(self.btn_res)
        self.fl.add_widget(self.anch_res)
        Window.clearcolor = [0, 0, 0, 1]
        self.fl.remove_widget(self.anch_hide)
        self.btns.append(self.btn01)
        self.fl.add_widget(self.btn01)
        self.fl.add_widget(self.btn02)
        return self.fl


if __name__ == '__main__':
    MyApp().run()
