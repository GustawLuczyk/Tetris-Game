import pytest
from events import *


def test_equeue_creation():
    ''' Sprawdzanie czy poprawnie tworzona jest kolejka zdarzen
    '''
    queue = EventsQueue()
    assert isinstance(queue, EventsQueue)
    assert not queue.remove()
    

def test_equeue_get_event_empty_queue():
    '''Sprawdzenie czy pusta kolejka zwroci
    zadrzenie NoEvent
    '''
    q = EventsQueue()
    assert isinstance(q.event, NoEvent)
    

def test_equeue_set_event_not_correct():
    ''' Sprawdzenie czy zglosi wyjatek AssertError
    gdy proba przypisania do zdarzenia obiektu nie bedacego
    typem pochodzacym od Event
    '''
    q = EventsQueue()
    with pytest.raises(AssertionError):
        q.event = 3
        

def test_equeue_set_event_correct():
    ''' Sprawdzenie czy nie bedzie problemu z 
    przypisaniem zdarzenia do kolejki
    '''
    q = EventsQueue()
    q.event = Event()
    q.event = NoEvent.NoEvent
    


def test_equeue_correct_elements_order():
    ''' Sprawdzenie czy nie bedzie problemu z 
    przypisaniem zdarzenia do kolejki, czy bedzie ich poprawna liczba
    i kolejnosc w kolejce ich przechowywania sie zgadza
    '''
    q = EventsQueue()
    q.event = Event()        # 1 - element
    q.event = NoEvent.NoEvent      # 2 - element
    q.event = Event()        # 3 - element

    assert isinstance(q.event, Event)    # sprawdzenie czy 1 element sie zgadza
    assert q.remove()                       # usuniecie 1 elementu

    assert isinstance(q.event, NoEvent)  # sprawdzenie czy 2 element sie zgadza
    assert q.remove()                       # usuniecie 2 elementu
    
    assert isinstance(q.event, Event)
    assert q.remove()

    assert isinstance(q.event, NoEvent)  # sprawdzenie ze jak kolejka pusta
                                            # to ma zwrocic NoEvent

    assert not q.remove()                   # Sprawdzenie ze remove ma zwrocic false
                                            # gdy kolejka pusta                       
    
        

