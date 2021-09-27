from events import *
import pygame

class PygameEvent(Event):
    '''Klasa zdarzen pochodzacych od pygame
    '''
    __slots__ = ["__event"]
    
    def __init__(self, ev):
        self.__event = ev
    
    @property
    def pgevent(self):
        return self.__event
    
    @pgevent.setter
    def pgevent(self, ev):
        self.__event = ev

     
class PygameProcess(EventsProcessor):
    '''Klasa pobierajace zdarzenia z pygames
    i jesli naleza do odpowiednich typow
    sa wstawiane do kolejki zdarzen
    '''
    
    def process(self, ev):
        assert isinstance(ev, EventsQueue), "Error: events not an object of EventsQueue"
        
        head = ev.event
        if isinstance(head, PygameEvent):
            ev.remove()
            
        for pgevent in pygame.event.get():
            if pgevent.type == pygame.QUIT:
                ev.event = PygameEvent(pgevent)
            elif pgevent.type == pygame.KEYDOWN:
                ev.event = PygameEvent(pgevent)
            elif pgevent.type == pygame.KEYUP:
                ev.event = PygameEvent(pgevent)
            elif pgevent.type == pygame.MOUSEBUTTONDOWN:
                ev.event = PygameEvent(pgevent)