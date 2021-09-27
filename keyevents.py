from enum import Enum, IntEnum, unique, auto
from pygame.constants import KEYDOWN
from events import *

@unique
class KeyType(Enum):
    '''Klasa stalych okreslajacych klawisze
    '''
    NONE = auto()
    EXIT = auto()
    LEFT = auto()
    RIGHT = auto()
    UP = auto()
    DOWN = auto()
    
@unique
class KeyState(Enum):
    '''Klasa stalych okreslajacych stan klawisza
    '''
    NONE = auto()
    UP = auto()
    DOWN = auto()
    

class KeyEvent(Event):
    '''Klasa zdarzenia klawisza
    '''
    __slots__ = ["__key_type", "__key_state"]
    
    def __init__(self):
        self.__key_state = KeyState.NONE
        self.__key_type = KeyType.NONE
        
    @property 
    def key(self):
        return self.__key_type
    
    @key.setter
    def key(self, kk):
        assert isinstance(kk, KeyType), "Error: Unknown key type"
        self.__key_type = kk
    
    @property 
    def state(self):
        return self.__key_state
    
    @state.setter
    def state(self, st):
        assert isinstance(st, KeyState), "Error: Unknown key state"
        self.__key_state = st
    
class KeyProcess(EventsProcessor):
    '''Klasa przetwarzajaca zdarzenia 
    '''
    __slots__ = ["__keys"]
    
    def __init__(self):
        self.__keys = dict()
        for key in KeyType:
            self.__keys[key] = KeyState.NONE
    
    def process(self, events):
        '''Funkcja przetwarzajaca zdarzenia w kolejce zdarzen
        Dodaje do kolejki zdarzenia KeyEvents kiedy pojawia sie 
        zdarzenia TICK
        '''
        assert isinstance(events, EventsQueue), "Error: events not an object of EventsQueue"
        ev = events.event
        