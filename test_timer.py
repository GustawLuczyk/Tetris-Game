from timer import *
from events import *
import pytest
import time


def test_timer_creation():
    '''Test tworzenia obiektu Timer
    '''
    tr = Timer()
    assert isinstance(tr, Timer)
    assert tr._Timer__tinyTime == 0.2
    assert tr._Timer__smallTime == 0.5
    assert tr._Timer__normalTime == 1
  

def test_timer_process_bad_queue():
    '''Test czy wykryje zly obiekt kolejki zdarzen
    '''
    tr = Timer()
    with pytest.raises(AssertionError):
        tr.process(2)
        
def test_timer_reset():
    '''Test resetu timera
    '''
    tr = Timer()
    tr.reset(normal_time=1, small_time=0.05, tiny_time=0.01)
    assert tr._Timer__tinyTime == 0.01
    assert tr._Timer__smallTime == 0.05
    assert tr._Timer__normalTime == 1

    
def test_timer_process():
    '''Test czy w kolejce zdarzen zostana wstawione po kolei 
    zdarzenia Tick: tiny, small i normal gdy uplynie odpowiednio dlugi czas.
    
    Sprawdzenie czy zdarzenia czasowe na poczatku kolejki sa usuwane z kolejki
    '''
    tr = Timer()
    events = EventsQueue()
    tr.reset(normal_time=0.1, small_time=0.05, tiny_time=0.02)
    step = 0.2
    time.sleep(step)
    tr.process(events)  # w kolejce powinny sie pojawic 
                        # w kolejnosci Tiny, Small, Normal Ticks
    
    assert events.event == TimerEvent.TinyTick  # Sprawdzenie czy TinyTick
    assert events.remove()                      # Usuniecie tiny Tick
    
    assert events.event == TimerEvent.SmallTick
    assert events.remove()                      # Usuniecie smallTick
    assert events.event == TimerEvent.NormalTick
    assert events.remove()  
    
    assert not events.remove()    # kolejka powinna byc pusta
    
def test_timer_remove_old_tick(capsys):
    '''Sprawdzenie czy stare zdarzenia sa usuwane
    '''
    
    tr = Timer()
    events = EventsQueue()
    tr.reset(normal_time=1, small_time=0.5, tiny_time=0.01)
    step = 0.01
    for i in range(10):
        time.sleep(step)
        tr.process(events)
    
    assert events.event == TimerEvent.TinyTick
    tr.process(events)
    assert isinstance(events.event,NoEvent)
    
    #print(events._EventsQueue__queue)
    #assert capsys.readouterr().out == ""
    