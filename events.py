from abc import abstractmethod
from enum import Enum, IntEnum, unique, auto

class Event(object):
    '''Klasa podstawowa dla wszystkich zdarzen
    '''
    pass

@unique
class NoEvent(Event, Enum):
    '''Klasa pochodna zdarzenia - brak zdarzenia
    '''
    NoEvent = auto()

class EventsProcessor(object):
    '''Klasa abstrakcyjna dla wszystkich klas 
    tworzacych/odbierajacych zdarzenia
    '''
    @abstractmethod
    def process(self, eventQueue):
        '''Metoda abstrakcyjna - musi byc zaimplementowana w klasie pochodnej
        '''
        pass

class EventsQueue(object):
    '''Klasa implementujaca kolejke FIFO zdarzen - oboiektow klasy Event
    Obiekt tej klasy jest odpowiedzialny za przekazywanie poszczegolnym
    obiektom zdarzenia do procezsowania - obiekty pochodne klasy EventProcessor
    '''
    
    # Klasa definiuje tylko 3 atrybuty 
    # wykorzystujac konstrukcje __slots__ aby zaoszczedzic miejsca w pamieci
    __slots__ = ['__head', '__tail', '__queue']
    
    def __init__ (self):
        '''Konstrukcja obiektu - wskazniki head i tail 
        sa ustawiane na 0
        '''
        super().__init__()
        self.__head = 0
        self.__tail = 0
        self.__queue = {}
        
    
    @property
    def event(self):
        ''' Wlasnosci (property). Zddefiniowany getter zwracajacy
        zdarzenie Event na poczatku kolejki zdarzen
        Jesli kolejka jest pusta to zwraca zdarzenie NoEvent
        '''
        if len(self.__queue.keys()) == 0:
            self.__head = 0
            self.__tail = 0
            return NoEvent.NoEvent
        else:
            return self.__queue[self.__head]
    
    @event.setter
    def event(self, ev):
        ''' Setter wlasnosci event
        Umozliwia wstawienie nowego zdarzenia do kolejki
        '''
        assert isinstance(ev, Event), "Error: EventQueue.setter - Not an Event based object"
        self.__queue[self.__tail] = ev
        self.__tail += 1
            
    def remove(self):
        '''Usuwa zdarzenie z poczatku kolejeki i zwraca True
        Jesli brak zdarzenia to zwraca False
        '''
        if len(self.__queue.keys()) == 0:
            self.__head = 0
            self.__tail = 0
            return False
        else:
            self.__queue.pop(self.__head)
            self.__head += 1
            return True
    
    def add(self, ev):
        '''Funkcja pomocnicza dodawania zdarzenia do kolejki
        Wykorzystuje event.setter
        '''
        self.event = ev
        

