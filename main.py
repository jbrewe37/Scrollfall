import json, requests, random, os, sys
import kivy
from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.clock import Clock
from kivy.config import Config
from kivy.resources import resource_add_path, resource_find
Config.set('graphics', 'width', '430')

class CarouselApp(App):
    def __init__(self, **kwargs):
        super(CarouselApp, self).__init__(**kwargs)
        self.carousel = 0
        self.current_slide = 0
    
    def build(self):
        self.icon = 'Scrollfall_icon.png'
        self.carousel = Carousel(direction='right', loop=False)

        found_card = 0
        while found_card == 0:
            try:
                url = 'https://api.scryfall.com/cards/random'
                r = requests.get(url, allow_redirects=True)
                rj = r.json()
                src = rj['image_uris']['large']
                found_card = 1
            except:
                pass
        new = AsyncImage(source=src, allow_stretch=True, keep_ratio=True)
        self.carousel.add_widget(new)

        found_card = 0
        while found_card == 0:
            try:
                url = 'https://api.scryfall.com/cards/random'
                r = requests.get(url, allow_redirects=True)
                rj = r.json()
                src = rj['image_uris']['large']
                found_card = 1
            except:
                pass
        new = AsyncImage(source=src, allow_stretch=True, keep_ratio=True)
        self.carousel.add_widget(new)
        
        found_card = 0
        while found_card == 0:
            try:
                url = 'https://api.scryfall.com/cards/random'
                r = requests.get(url, allow_redirects=True)
                rj = r.json()
                src = rj['image_uris']['large']
                found_card = 1
            except:
                pass
        new = AsyncImage(source=src, allow_stretch=True, keep_ratio=True)
        self.carousel.add_widget(new)

        event = Clock.schedule_interval(self.my_callback, 1/5)

        self.current_slide = self.carousel.current_slide
        
        return self.carousel

    def my_callback(self, dt):
        if self.carousel.current_slide != self.current_slide:
            self.current_slide = self.carousel.current_slide
            found_card = 0
            while found_card == 0:
                try:
                    url = 'https://api.scryfall.com/cards/random'
                    r = requests.get(url, allow_redirects=True)
                    rj = r.json()
                    src = rj['image_uris']['large']
                    found_card = 1
                except:
                    pass
            new = AsyncImage(source=src, allow_stretch=True, keep_ratio=True)
            self.carousel.add_widget(new)

if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    CarouselApp().run()
