from events import *
import time
from enum import Enum, IntEnum, unique, auto

@unique
class TimerEvent(Event, Enum):
    '''Klasa zdarzenia czasowego
    '''
    TinyTick = auto()
    SmallTick = auto()
    NormalTick = auto()


class Timer(EventsProcessor):
    '''Klasa realizująca timer, ktory wysyla do kolejki zdarzen
    zdarzenia TICK: tiny, small, normal w zaleznosci od czasu
    '''
    __slots__ = [
                 # zmienne przechowujace odstepy czasowe zdarzen :
                 "__tinyTime",      # TinyTick
                 "__smallTime",     # SmallTick
                 "__normalTime",    # NormalTick
                 
                 # zmienne przechowujace czas ostatnio zgloszonego zdarzenia
                 "__time_normal",   # NormalTick
                 "__time_tiny",     # TinyTick
                 "__time_small"     # SmallTick
                 ]
    
    def __init__(self):
        super().__init__()
        self.reset()
        
    def reset(self, normal_time = 1, small_time=0.5, tiny_time=0.2):
        '''Funkcja zeruje Timer i ew. ustawia czasy dla poszczegolnych
        zdarzen TimeTick
        '''
        self.__tinyTime   = float(tiny_time)
        self.__smallTime  = float(small_time)
        self.__normalTime = float(normal_time)
        
        tm = time.time()
        self.__time_normal = tm
        self.__time_tiny = tm
        self.__time_small = tm
        
    def process(self, events):
        '''Funkcja przetwarzajaca zdarzenia w kolejce zdarzen
        Dodaje do kolejki zdarzenia TICK
        Usuwa z kolejki stare zdarzenia TICK
        '''
        assert isinstance(events, EventsQueue), "Error: events not an object of EventsQueue"
        ev = events.event
        if isinstance(ev, TimerEvent):
            events.remove()
        
        time_now = time.time()

        if time_now - self.__tinyTime > self.__time_tiny:
            events.event = TimerEvent.TinyTick
            self.__time_tiny = time_now

        if time_now - self.__smallTime > self.__time_small:
            events.event = TimerEvent.SmallTick
            self.__time_small = time_now
            
        if time_now - self.__normalTime > self.__time_normal:
            events.event = TimerEvent.NormalTick
            self.__time_normal = time_now
            
        
